from dash import Dash, html, dash_table, callback, dcc
from dash.dependencies import Input, Output
from sklearn.linear_model import LinearRegression
import json
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import numpy as np
import random


def load_and_prepare_data():
    data = pd.read_csv("cars.csv")

    # Informace o prodejci nas nezajimaji
    data = data.drop(columns=['seller_name', 'seller_rating'])

    # Price drop je sloupec, ktery obsahuje obrovske mnozstvi Nan hodnot
    # Bude jednodussi se jim nezabyvat
    data = data.drop(columns=['price_drop'])

    data.fuel_type.unique()

    # Pro elektricke a hybridni vozy byla casto hodnota mpg NaN
    # Proto jsem se ji rozhodl nahradit nulou
    electric_list = ['Hybrid', 'Electric', 'Gasoline/Mild Electric Hybrid', 'Compressed Natural Gas',
                     'Hydrogen Fuel Cell', 'PHEV', 'Hybrid Fuel', 'Electric Fuel System', 'Gas/Electric Hybrid',
                     'Plug-In Electric/Gas']
    data.loc[(data['mpg'].isnull()) & (data['fuel_type'].isin(electric_list)), 'mpg'] = '0'

    # Pocet radku, pocet radku s nejakym NaN
    # Dataset je dost velky, abych mohl NaN radky dropnout bez nahrazovani apod.
    print(data.shape[0])
    print(data.shape[0] - data.dropna().shape[0])

    df = data.dropna()

    print(df.shape[0])
    print(df.shape[0] - df.dropna().shape[0])

    # Konverze float promennych na int
    df = df.astype({"mileage": 'int', "accidents_or_damage": 'int', "one_owner": 'int',
                    "personal_use_only": 'int', "driver_reviews_num": 'int', "price": 'int'})

    df.mpg.unique()

    # Kod z ChatGPT: prevod mnoha ruznych hodnot mpg do 10 intervalu
    df_copy = df.copy()

    # Define a function to convert each value to a unified range
    def convert_to_unified_range(value):
        try:
            # Try to convert the value to float
            float_value = float(value)
            return float_value
        except ValueError:
            # If conversion to float fails, it means it's a range; take the average
            start, end = map(float, value.split('-'))
            avg_value = (start + end) / 2
            return avg_value

    # Apply the conversion function to the 'mpg_column' in the DataFrame
    df_copy['mpg_range'] = df_copy['mpg'].apply(convert_to_unified_range)
    # Define your desired ranges
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # Create labels for the ranges
    labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
    # Cut the data into the specified ranges
    df_copy['mpg_range'] = pd.cut(df_copy['mpg_range'], bins=bins, labels=labels, include_lowest=True)

    # Par kategorii jsou NaN, protoze jejich puvodni hodnota mpg byla nesmysl
    len(df_copy.loc[(df_copy['mpg_range'].isnull())])
    df_copy = df_copy.dropna()
    df_copy.mpg_range.unique()

    # Odstraneni puvodniho mpg sloupce
    df_final = df_copy.drop(columns=['mpg'])

    # Poradi sloupcu
    df_final = df_final[['manufacturer', 'model', 'year', 'mileage', 'price', 'engine', 'transmission', 'drivetrain',
                         'fuel_type', 'mpg_range', 'exterior_color', 'interior_color', 'accidents_or_damage',
                         'one_owner', 'personal_use_only', 'driver_rating', 'driver_reviews_num']]

    # Na konci mame 565 746 radku, 17 promennych a zadne NaN
    return df_final


def dataset_for_visualization(df):
    # Puvodni dataset je prilis velky pro vizualizaci. Zamichame poradi, vybereme prvnich 10tis. radku a seradime
    df_final = df.sample(frac=1).reset_index(drop=True)
    return df_final.iloc[0:10_000].sort_values(by=['manufacturer'], ascending=True)


def create_linear_regression(df):
    # Uplne zakladni linearni regrese z jedne ciselne a tri binarnich promennych
    X = df[['year', 'accidents_or_damage', 'one_owner', 'personal_use_only']]
    y = df['price']
    reg = LinearRegression().fit(X, y)
    # Vypocet MAPE
    print(np.mean([np.abs(i - j) / j for i, j in zip(reg.predict(X), y)]))
    return reg


random.seed(10)
big_df = load_and_prepare_data()
reg = create_linear_regression(big_df)
small_df = dataset_for_visualization(big_df)
helper_price_prediction = 0  # Tohle je hnus, ale nastesti mi to nepusobilo zadne potize

app = Dash(external_stylesheets=[dbc.themes.FLATLY])

# Pojmenovani sloupcu pro tabulku
col_names = ['Manufacturer', 'Model', 'Production Year', 'Mileage', 'Price', 'Engine', 'Transmission', 'Drivetrain',
             'Fuel Type', 'Miles Per Gallon', 'Exterior Color', 'Interior Color', 'Damaged', 'One Owner',
             'Personal Use', 'Rating', 'Number of Reviews']
# Typy sloupcu pro Dash DataTable
col_types = ['text', 'text', 'numeric', 'numeric', 'text', 'text', 'text', 'text', 'text', 'text', 'text', 'text',
             'numeric', 'numeric', 'numeric', 'numeric', 'numeric']
# Tvorba sloupcu z jmen pro zobrazeni, puvodnich sloupcu dataframu a datovych typu
columns = [{'name': x, 'id': y, 'type': z} for x, y, z in zip(col_names, list(small_df.columns), col_types)]

# Tabulka
table = dash_table.DataTable(data=small_df.to_dict('records'), columns=columns,
                             page_size=15, style_table={'overflowX': 'auto'},
                             filter_action='native', filter_options={'case': 'insensitive'},
                             style_header={'fontWeight': 'bold', 'font-family': 'sans-serif'},
                             style_cell={'font-family': 'sans-serif'},
                             sort_action='native', id='datatable', style_data_conditional=[{'if':
                                                                                                {'row_index': 'odd'},
                                                                                            'backgroundColor': 'rgb('
                                                                                                               '211, '
                                                                                                               '225, '
                                                                                                               '237)'}])
# Tabulka za pouziti Bootstrap Componentu mi bohuzel nejak nefunfovala
# table2 = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

# Inputy pro linearni regresi
prediction_input_group = html.Div(
    [
        dbc.InputGroup([dbc.InputGroupText("Year of production"), dbc.Input(id='year-input',
                                                                            type="number",
                                                                            value=2010,
                                                                            min=1900,
                                                                            max=2023,
                                                                            step=1
                                                                            )]),
        dbc.InputGroup([
            dbc.InputGroupText("Damaged"),
            dbc.Checklist(options=[''], value=[], id="damaged-checklist", ),
        ]),
        dbc.InputGroup([
            dbc.InputGroupText("One owner"),
            dbc.Checklist(options=[''], value=[], id="owner-checklist", ),
        ]),
        dbc.InputGroup([
            dbc.InputGroupText("Personal use only"),
            dbc.Checklist(options=[''], value=[], id="personal-checklist", ),
        ])
    ], style={'width': '30%'}
)

# Cast doporuceni auta
recommended_car_section = html.Div([
    html.Br(),
    html.Br(),
    html.H4('Your recommended car at this price is:'),
    html.Div(id='recommended-car-output')
])

app.layout = html.Div([
    html.H1('MDIP Dashboard: Used Cars', style={"padding": "20px"}),
    html.Br(),
    html.Div([
        table
    ], style={"padding": "10px"}),
    html.H3('Price distribution', style={"padding": "40px"}),
    dcc.Graph(id='graph-price'),
    html.H3('Mileage distribution', style={"padding": "40px"}),
    dcc.Graph(id='graph-mileage'),
    html.H3('Manufacturer distribution', style={"padding": "40px"}),
    dcc.Graph(id='graph-manufacturer'),
    html.Div([
        html.Div([
            html.H3('Price prediction'),
            html.H5(id='prediction-result'),
            html.Br(),
            prediction_input_group,
            html.Br(),
            html.Br(),
        ],
            style={"width": "50%",
                   "float": "left",
                   "padding": "20px"}),
        html.Div([
            recommended_car_section
        ],
            style={"width": "50%",
                   "float": "left",
                   "padding": "20px"})
    ], style={"border": "3px solid #fff",
              "padding": "20px"}),
    dcc.Store(id='recommended-car')
])


# Callback pro graf cen
@callback(
    Output('graph-price', 'figure'),
    Input('datatable', "derived_virtual_data"))
def update_price_graph(rows):
    # Pokud se nepodari nacist radky z DataTable/jsou null, pouzije se cely dataset
    dff = small_df if rows is None else pd.DataFrame(rows)

    fig = go.Figure()

    fig.add_trace(go.Histogram(x=dff['price'], marker=dict(color='rgb(29,84,122)')))
    fig.update_layout(xaxis_title="Price in USD",
                      yaxis_title="Number of cars")

    return fig


# Callback pro graf najezdu
@callback(
    Output('graph-mileage', 'figure'),
    Input('datatable', "derived_virtual_data"))
def update_mileage_graph(rows):
    # Pokud se nepodari nacist radky z DataTable/jsou null, pouzije se cely dataset
    dff = small_df if rows is None else pd.DataFrame(rows)

    fig = go.Figure()

    fig.add_trace(go.Histogram(x=dff['mileage'], marker=dict(color='rgb(44,127,184)')))
    fig.update_layout(yaxis_title="Number of cars",
                      xaxis_title="Mileage")

    return fig


# Callback pro graf vyrobcu
@callback(
    Output('graph-manufacturer', 'figure'),
    Input('datatable', "derived_virtual_data"))
def update_manufacturer_graph(rows):
    # Pokud se nepodari nacist radky z DataTable/jsou null, pouzije se cely dataset
    dff = small_df if rows is None else pd.DataFrame(rows)

    fig = go.Figure()

    fig.add_trace(go.Histogram(x=dff['manufacturer'], histfunc="count", marker=dict(color='rgb(65,182,196)')))
    fig.update_layout(yaxis_title="Number of cars",
                      xaxis_title="Manufacturer")

    return fig


# Callback pro vypocet predikce
@callback(
    Output("prediction-result", "children"),
    Input("year-input", "value"),
    Input("damaged-checklist", "value"),
    Input("owner-checklist", "value"),
    Input("personal-checklist", "value"))
def predict_price(year_input, damaged_checklist, owner_checklist, personal_checklist):
    damaged_bool = len(damaged_checklist) != 0
    owner_bool = len(owner_checklist) != 0
    personal_bool = len(personal_checklist) != 0

    X = pd.DataFrame()
    X['year'] = [year_input]
    X['accidents_or_damage'] = [int(damaged_bool)]
    X['one_owner'] = [int(owner_bool)]
    X['personal_use_only'] = [int(personal_bool)]

    prediction = reg.predict(X)

    # Ulozeni predikovane ceny do globalni promenne pro pouziti v recommendation
    global helper_price_prediction
    helper_price_prediction = prediction[0]

    return f"Predicted price: {int(prediction[0]):,} USD"


# Callback pro doporuceni auta. Vraci dictionary jednoho auta v json stringu
@callback(
    Output("recommended-car", "data"),
    Input("year-input", "value"),
    Input("damaged-checklist", "value"),
    Input("owner-checklist", "value"),
    Input("personal-checklist", "value"),
    prevent_initial_call=True)
def recommend_car(year_input, damaged_checklist, owner_checklist, personal_checklist):
    damaged_bool = len(damaged_checklist) != 0
    owner_bool = len(owner_checklist) != 0
    personal_bool = len(personal_checklist) != 0

    if helper_price_prediction == 0:
        return

    matching_cars = big_df.loc[(big_df['year'] >= year_input) &
                               (big_df['price'] <= helper_price_prediction) &
                               (big_df['accidents_or_damage'] == int(damaged_bool)) &
                               (big_df['one_owner'] == int(owner_bool)) &
                               (big_df['personal_use_only'] == int(personal_bool))]

    # Spagety
    if len(matching_cars) > 0:
        matching_cars_4_plus = matching_cars.loc[matching_cars['driver_rating'] >= 4]
        if len(matching_cars_4_plus) > 0:
            random_row = matching_cars_4_plus.sample().to_dict('records')[0]
        else:
            matching_cars_3_plus = matching_cars.loc[matching_cars['driver_rating'] >= 3]
            if len(matching_cars_3_plus) > 0:
                random_row = matching_cars_3_plus.sample().to_dict('records')[0]
            else:
                random_row = matching_cars.sample().to_dict('records')[0]
        return json.dumps(random_row)
    else:
        return


# Callback pro formatovani doporuceneho auta. Inputem je json string z minule funkce
@callback(
    Output("recommended-car-output", "children"),
    Input("recommended-car", "data"),
    prevent_initial_call=True
)
def return_formatted_recommended_car(json_data):
    recommended_car = json.loads(json_data)
    print(recommended_car)
    google_url = "https://www.google.com/search?q="
    url_params = f"{recommended_car['manufacturer'].replace(' ', '+')}+{recommended_car['model'].replace(' ', '+')}+year+{recommended_car['year']}"

    return html.Div([
        html.H5(f"{recommended_car['manufacturer']} {recommended_car['model']}"),
        html.H5(f"Year of production: {recommended_car['year']}"),
        html.H5(f"Mileage: {recommended_car['mileage']:,}"),
        html.H5(f"Price: {recommended_car['price']:,}"),
        html.Br(),
        html.A("Search this car on the web", href=google_url + url_params)
    ])


app.run_server(debug=True)
