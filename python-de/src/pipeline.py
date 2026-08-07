import csv

class DataPipeline:
    # Initialization
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    
    # Extract the data
    def extract_data(self) -> list[dict]:
        print(f"Extracting data from {self.source}")
        data = []

        with open(self.source, "r", newline = "", encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for raw in reader:
                data.append(raw)
    
        return data

    # Transform the data
    def transform_data(self, data:list[dict]) -> list[dict]:
        print("Transforming data")
        cleaned_data = []

        for row in data:
            if row["amount"] not in [None, "", "NULL"]:
                row["amount"] = float(row["amount"])
                cleaned_data.append(row)
        
        return cleaned_data
    
    # Load the data to destination
    def load_data(self, data: list[dict]) -> None:
        print(f"Loading {len(data)} records to {self.destination}")
        
        if not data: # checks if the data is empty or not
            print("No data to write.")
            return
        
        with open(self.destination, "w", newline = "", encoding = "utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        
    # Orchestrate the flow - the class needs to be called & the run() function needs to run
    def run(self):
        extracted_data = self.extract_data() # extract the data
        transformed_data = self.transform_data(extracted_data) # transform the data
        self.load_data(transformed_data) # load the data

# Calling the DataPipeline class to run the whole process
desired_source = "data/raw/dirty_orders.csv"
desired_destination = "data/cleaned/cleaned_orders.csv"
pipeline = DataPipeline(desired_source, desired_destination)
pipeline.run()