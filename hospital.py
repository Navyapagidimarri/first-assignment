class Hospitalmanagement:
    def __init__(self):
        self.d = {}

    def management(self):
        while True:
            print("Choose Option")
            print("1) Entry details")
            print("2) Display data")
            print("3) Search by ID")
            print("4) Delete the patient details after discharge")
            print("5) Update Patient Details")
            print("6) Exit")

            choose_option = int(input("Select an option (1/2/3/4/5/6): "))

            if choose_option == 1:
                self.marolix_hospital()
            elif choose_option == 2:
                self.display_details()
            elif choose_option == 3:
                self.search_by_id()
            elif choose_option == 4:
                self.delete_patient()
            elif choose_option == 5:
                self.update_patient_details()
            elif choose_option == 6:
                print("Exiting!")
                break
            else:
                print("Invalid option. Please select a valid option (1/2/3/4/5/6).")

    def marolix_hospital(self):
        patients_entry = int(input("Enter the number of patients: "))
        for i in range(patients_entry):
            patients_name = input("Enter patient's name: ")
            patients_issue = input("Enter patient's issue: ")
            patients_id = input("Enter patient's ID: ")
            patients_mobilenumber = input("Enter patient's mobile number: ")
            patients_joining_date = input("Enter patient's joining date format (DD-MM-YYYY): ")
            self.d[patients_name] = {
                'Issue': patients_issue,
                'ID': patients_id,
                'Mobile Number': patients_mobilenumber,
                'Joining Date': patients_joining_date
            }
        print("Patient details have been added.")
    def display_details(self):
        print("To Display patients details:")
        print("Patients details:")
        print("*****************")
        for patient_name, patient_info in self.d.items():
            print("Patient Name:", patient_name)
            print("Patient ID:", patient_info['ID'])
            print("Patient Mobile Number:", patient_info['Mobile Number'])
            print("Patient Issue:", patient_info['Issue'])
            print("Patient Joining Date:", patient_info['Joining Date'])
            print("*****************")
    def search_by_id(self):
        search_patients_id = input("Enter a patient's ID to search: ")
        found = False
        for patient_name, patient_info in self.d.items():
            if patient_info['ID'] == search_patients_id:
                print("Patient Name:", patient_name)
                print("Patient ID:", patient_info['ID'])
                print("Patient Mobile Number:", patient_info['Mobile Number'])
                print("Patient Issue:", patient_info['Issue'])
                print("Patient Joining Date:", patient_info['Joining Date'])
                found = True
        if not found:
            print("No patient found with the given ID.")
    def delete_patient(self):
        patient_name = input("Enter patient's name to remove: ")
        if patient_name in self.d:
            del self.d[patient_name]
            print(f"{patient_name}'s data has been deleted.")
        else:
            print(f"No patient found with the name {patient_name}.")
    def update_patient_details(self):
        patient_name = input("Enter patient's name to update details: ")
        if patient_name in self.d:
            print(f"Update details for {patient_name}:")
            patients_issue = input("Enter updated issue: ")
            patients_id = input("Enter updated ID: ")
            patients_mobilenumber = input("Enter updated mobile number: ")
            patients_joining_date = input("Enter updated joining date format (DD-MM-YYYY): ")
            self.d[patient_name]['Issue'] = patients_issue
            self.d[patient_name]['ID'] = patients_id
            self.d[patient_name]['Mobile Number'] = patients_mobilenumber
            self.d[patient_name]['Joining Date'] = patients_joining_date
            print("patientss details have been updated.")
        else:
            print(f"No patient found with the name {patient_name}.")
filter_details = Hospitalmanagement()
filter_details.management()
