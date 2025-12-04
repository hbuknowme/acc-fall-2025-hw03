from src.homework.h_strings.value_return import get_hamming_distance, get_dna_complement

def menu():
    while True:
        print("\nMenu:")
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            dna1 = input("Enter first DNA string: ")
            dna2 = input("Enter second DNA string: ")
            print("Hamming Distance:", get_hamming_distance(dna1, dna2))

        elif choice == '2':
            dna = input("Enter DNA string: ")
            print("DNA Complement:", get_dna_complement(dna))

        elif choice == '3':
            print("Exiting program...")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    menu()
