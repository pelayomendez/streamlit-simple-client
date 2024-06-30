import streamlit as st
import requests
import os

# Define the base URL of the Pokemon API
BASE_URL = "https://pokeapi.co/api/v2"

# Define the base URL of the Pokemon API
DEFAULT_POKEMON_NAME = os.environ.get('DEFAULT_POKEMON_NAME')


# Function to make an HTTP GET request to the Pokemon API
def get_pokemon_data(pokemon_name):
    url = f"{BASE_URL}/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit app code
def main():
    st.title("Pokemon API Example")
    pokemon_name = st.text_input("Enter a Pokemon name:", value=DEFAULT_POKEMON_NAME or "charizard")
    if st.button("Get Pokemon Data"):
        if pokemon_name:
            pokemon_data = get_pokemon_data(pokemon_name)
            if pokemon_data:
                st.write("Pokemon Name:", pokemon_data["name"])
                st.write("Pokemon ID:", pokemon_data["id"])
                st.write("Pokemon Height:", pokemon_data["height"])
                st.write("Pokemon Weight:", pokemon_data["weight"])
            else:
                st.write("Pokemon not found!")
        else:
            st.write("Please enter a Pokemon name.")

if __name__ == "__main__":
    main()