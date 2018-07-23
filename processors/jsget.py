import click
import sys
from selenium import webdriver
from time import sleep

@click.command()
@click.argument('URL')
@click.option('--output','-o')
def main(output,url=''):
    chrome_options = webdriver.chrome.options.Options()  
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    print(f'Downloading {output}...')
    driver.get(url)
    html = driver.page_source
    if(output):
        with open(output,'w') as f:
            f.write(html)
    else:
        sys.stdout.write(html)
    driver.close()

if __name__ == "__main__":
    main()