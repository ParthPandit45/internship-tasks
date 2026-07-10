# Base class
class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state
        
    def get_full_address(self):
        address_str = f"{self.city}, {self.state}"
        return address_str

# Base class
class Worker:
    def get_info(self):
        raise NotImplementedError()

# Child class
class Employee(Worker):
    def __init__(self, name, emp_id, base_salary, address):
        self.name = name
        self.base_salary = base_salary
        self.__emp_id = emp_id 
        self.address = address
        
    def get_emp_id(self):
        return self.__emp_id
        
    def get_info(self):
        emp_id = self.get_emp_id()
        addr_str = self.address.get_full_address()
        info_str = f"Employee: {self.name} (ID: {emp_id}) Location: {addr_str}"
        return info_str
        
    def calculate_pay(self):
        tax_amount = self.base_salary * 0.20
        net_pay = self.base_salary - tax_amount
        return net_pay

# Child class
class Manager(Employee):
    def __init__(self, name, emp_id, base_salary, address, bonus):
        super().__init__(name, emp_id, base_salary, address)
        self.bonus = bonus
        
    def calculate_pay(self):
        base_pay = super().calculate_pay()
        total_pay = base_pay + self.bonus
        return total_pay
        
    def get_info(self):
        emp_id = self.get_emp_id()
        addr_str = self.address.get_full_address()
        info_str = f"Manager: {self.name} (ID: {emp_id}) Location: {addr_str} Bonus: ${self.bonus}"
        return info_str

# Main function
def main():
    print("Welcome to the Payroll System")
    
    # Get inputs
    role = input("Enter role (employee/manager): ").strip().lower()
    name = input("Enter name: ")
    emp_id = input("Enter ID: ")
    base_salary = float(input("Enter base salary: "))
    
    city = input("Enter city: ")
    state = input("Enter state: ")
    
    # Setup addresses
    worker_addr = Address(city, state)

    # Setup workers
    if role == "manager":
        bonus = float(input("Enter bonus: "))
        worker = Manager(name, emp_id, base_salary, worker_addr, bonus)
    else:
        worker = Employee(name, emp_id, base_salary, worker_addr)

    # Print info
    worker_info = worker.get_info()
    print()
    print(worker_info)
    
    # Compute pay
    worker_pay = worker.calculate_pay()
    print(f"Net Pay: ${worker_pay}")

if __name__ == "__main__":
    main()
