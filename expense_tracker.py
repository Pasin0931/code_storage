category_name = []
category_value = []
category_limit = ["food", "transport", "entertainment", "shopping", "bills"]

def main():
    while True:
        try:
            print("\n====================")
            print("EXPENSE TRACKER MENU")
            print("====================")
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. View by Category")
            print("4. Spending Summary")
            print("5. Exit")
            
            if category_value == []:
                sum_value = 1
            else:
                sum_value = sum(category_value)
            
            choices_in = str(input("Enter your choice (1-5): "))
            
            if choices_in == "1":
                input_value = float(input("\nEnter amount: "))
                if type(input_value) == int or float:
                    input_cat = str(input("Enter category (food, transport, entertainment, shopping, bills): "))
                
                    if input_cat.lower() in category_limit:
                        category_name.append(input_cat.lower())
                        category_value.append(input_value)
                        # print(category_name)
                        # print(category_value)
                    else:
                        print("\n-- Please input a correct category ! --\n")
                    
                else:
                    print("\n-- Please input an integer ! --\n")
                    
            elif choices_in == "2":
                print("\n=== ALL EXPENSES ===")
                print("Category        Amount")
                print("---------------------------")
                if len(category_name) != 0:
                    for i in range(len(category_name)):
                        if len(category_name[i]) > 4:
                            minus = len(category_name[i]) - 4
                            decrease_space = 10 - minus
                            total_space = " " * decrease_space
                        else:
                            total_space = "          "
                        print(category_name[i], total_space, category_value[i])
                else:
                    print("\n-- No transactions --\n")
                print("---------------------------")
                print("TOTAL: $" + str(sum_value))
                
            elif choices_in == "3":
                print("\nCategories are food, transport, entertainment, shopping, bills")
                input_cata = str(input("Enter category to filter by: ")).lower()
                
                if (input_cata.lower() in category_limit):
                    sum_input_arr = []
                    print("=== EXPENSES FOR", input_cata, "===")
                    print("---------------------------")
                    for i in range(len(category_name)):
                        if category_name[i].lower() == input_cata:
                            sum_input_arr.append(category_value[i])
                            print("$" + str(category_value[i]))
                    if category_name == []:
                        print("\n-- No transactions --\n")
                    total_sum_input = sum(sum_input_arr)
                    print("---------------------------")
                    print("TOTAL: $" + str(total_sum_input))
                    print("---------------------------")
                    sum_input_arr = []
                
            elif choices_in == "4":
                sum_selected = []
                print("\n=== SPENDING SUMMARY ===")
                    
                for i in range(len(category_limit)):
                    if len(category_limit[i]) > 4:
                        minus = len(category_limit[i]) - 4
                        decrease_space = 10 - minus
                        total_space = " " * decrease_space
                    else:
                        total_space = "          "
                            
                    print(category_limit[i], total_space, ": $ ", end="")
                    
                    for j in range(len(category_name)):
                        if category_limit[i] == category_name[j]:
                            sum_selected.append(category_value[j])
                            
                    percentage = round(((sum(sum_selected) / sum_value) * 100), 2)
                    print(str(sum(sum_selected)), "(" + str(percentage) + "%)")

                    sum_selected = []
                
                print("-------------------------")
                if category_value == []:
                    sum_value = 0
                print("TOTAL           : $   " + str(sum_value))
                
            elif choices_in == "5":
                print("\n-- Exiting program --\n")
                break
            
            else:
                print("\n-- Wrong input ! --")
        except ValueError as e:
            print("Error !", e)
            
if __name__ == "__main__":
    main()