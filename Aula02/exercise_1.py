
def register_users():
    # Predefined users: (Name, Age, Is_Active)
    predefined_users = [
        ("Alice", 25, True),
        ("Bob", 17, False),
        ("Charlie", 15, True),
        ("Diana", 30, True),
        ("Eve", 12, False)
    ]

    print("--- User Registration System (Exercise 1) ---")
    for name, age, is_active in predefined_users:
        # Determine if adult or minor
        age_status = "maior de idade" if age >= 18 else "menor de idade"
        
        # Determine active status
        active_status = "ativo" if is_active else "inativo"
        
        print(f"Usuário: {name} | Idade: {age} ({age_status}) | Status: {active_status}")

if __name__ == "__main__":
    register_users()

def classify_age(age):
    if age <= 12:
        return "criança"
    elif age < 60:
        return "adulto"
    else:
        return "idoso"

def register_users_v2():
    # Predefined users with emails: (Name, Age, Is_Active, Email)
    # Intentionally including a duplicate email to demonstrate the uniqueness check
    predefined_users = [
        ("Alice", 25, True, "alice@example.com"),
        ("Bob", 10, False, "bob@example.com"),
        ("Charlie", 65, True, "charlie@example.com"),
        ("Diana", 30, True, "alice@example.com"),  # Duplicate email
        ("Eve", 8, False, "eve@example.com")
    ]

    registered_emails = set()
    print("--- User Registration System (Exercise 2) ---")
    
    for name, age, is_active, email in predefined_users:
        # Check for unique email
        if email in registered_emails:
            print(f"Erro: O email '{email}' já está em uso por outro usuário. Cadastro de {name} recusado.")
            continue
        
        registered_emails.add(email)
        
        # Classify based on age group
        age_group = classify_age(age)
        
        # Determine active status
        active_status = "ativo" if is_active else "inativo"
        
        print(f"Usuário: {name} | Email: {email} | Idade: {age} | Grupo: {age_group} | Status: {active_status}")

if __name__ == "__main__":
    register_users_v2()
