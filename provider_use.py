import logging
from providers.zonaprop import Zonaprop

# Assuming you have a setup function or config to initialize provider data
def setup_providers():
    provider_data = {
        'zonaprop': {
            'provider_data': {'base_url':'https://www.zonaprop.com.ar', 'sources':['/departamentos-alquiler-capital-federal.html']},
            'provider_name': 'Zonaprop'
        }
        # Add other providers here
    }

    providers = {
        'zonaprop': Zonaprop(**provider_data['zonaprop'])
        # Add other provider instances here
    }

    return providers

def main():
    logging.basicConfig(level=logging.INFO)
    providers = setup_providers()

    for provider_name, provider in providers.items():
        for source in provider.provider_data['sources']:
            logging.info(f"Scraping {source} with {provider_name}")
            for property_data in provider.props_in_source(source):
                process_property_data(property_data)  # Define this function to handle the data

def process_property_data(property_data):
    # Implement this function to save or process the scraped data
    print(property_data)

if __name__ == "__main__":
    main()
