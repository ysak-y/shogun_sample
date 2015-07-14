
def label_function():
    from modshogun import BinaryLabels
    from modshogun import CSVFile

    #generate random labels 
    label = BinaryLabels(5)

    print label.get_num_labels()
    #→ 5

    print label.get_values()
    #→ array([5 label values])

    label_from_csv = BinaryLabels(CSVFile("csv/label.csv"))


