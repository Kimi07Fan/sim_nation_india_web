import sys
import json
from utils import gen_html

def main():
    if len(sys.argv) != 2:
        print("Usage: python update_data.py <JSON configuration>")
        sys.exit(1)

    json_config = sys.argv[1]

    with open(json_config, 'r') as f:
        config = json.load(f)
    
    for config_item in config['configs_to_pick']:
        with open(config_item['JSON'], 'r') as f:
            print ("Reading configuration for league:", config_item['League'])
            league_config = json.load(f)
            gen_html.generate_html(league_config)
            
            # TODO: Update Driver Categorization since league data is being updated.

main()