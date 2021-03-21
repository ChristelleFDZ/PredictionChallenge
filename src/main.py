import utils


# -- coding: utf-8 --

def main():
    """ Main program """
    parser= utils.DataParsing('../resources','data.csv')
    result= parser.parseCSV()
    
    return 0

if __name__ == "__main__":

    main()
