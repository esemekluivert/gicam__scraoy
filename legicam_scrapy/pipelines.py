import csv

class CsvExportPipeline:
    def open_spider(self, spider):
        self.csv_file = open('members.csv', 'w', newline='')
        fieldnames = ['Name', 'Activities', 'Subsector Activities', 'PO Box', 'City', 'Fax', 'Email', 'Location', 'Manager']
        self.csv_writer = csv.DictWriter(self.csv_file, fieldnames=fieldnames)
        self.csv_writer.writeheader()

    def process_item(self, item, spider):
        # Create a dictionary for the item
        data = {
            'Name': item.get('name', 'None'),
            'Activities': item.get('activities', 'None'),
            'Subsector Activities': item.get('subsector_activities', 'None'),
            'PO Box': item.get('po_box', 'None'),
            'City': item.get('city', 'None'),
            'Fax': item.get('fax', 'None'),
            'Email': item.get('email', 'None'),
            'Location': item.get('location', 'None'),
            'Manager': item.get('manager', 'None'),
        }

        # Write the item to the CSV file as a dictionary
        self.csv_writer.writerow(data)
        return item

    def close_spider(self, spider):
        self.csv_file.close()
