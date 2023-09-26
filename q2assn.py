def encoded(encoded_str):
    parts = encoded_str.split('0')
    parts = [part for part in parts if part]
    if len(parts)<3:
        return None
    
    first_name = parts[0]
    last_name = parts[1]
    id_value = parts[2]
    
    result = {
        "first_name": first_name,
        "last_name": last_name,
        "id": id_value
    }
    
    return result

encoded_str = input("Enter your encoded string: ")
data = encoded(encoded_str)
if data is not None:
    print(data)
else:
    print("Invalid format")