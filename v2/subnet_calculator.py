# subnet_calculator.py

def ip_to_int(ip):
    """Convierte una dirección IP en su representación entera."""
    return sum(int(octet) << (8 * i) for i, octet in enumerate(reversed(ip.split('.'))))

def int_to_ip(num):
    """Convierte un entero en una dirección IP."""
    return '.'.join(str((num >> (8 * i)) & 255) for i in reversed(range(4)))

def calculate_subnet(ip_base, num_users):
    """Calcula la subred basada en la IP base y el número de usuarios."""
    try:
        ip_int = ip_to_int(ip_base)

        # Calcula el número de bits necesarios para representar los usuarios + 2 (red y broadcast)
        host_bits = (num_users + 2).bit_length()
        subnet_bits = 32 - host_bits

        if subnet_bits < 0:
            raise ValueError("La cantidad de usuarios excede el rango posible de direcciones IP.")
        
        # Calcula la máscara de subred
        subnet_mask = (0xFFFFFFFF << host_bits) & 0xFFFFFFFF
        network_address = ip_int & subnet_mask
        broadcast_address = network_address | (0xFFFFFFFF >> subnet_bits)
        
        first_usable = network_address + 1
        last_usable = broadcast_address - 1
        
        return {
            "Red base": int_to_ip(network_address),
            "Primera IP asignable": int_to_ip(first_usable),
            "Última IP asignable": int_to_ip(last_usable),
            "Broadcast": int_to_ip(broadcast_address),
            "Máscara de subred": int_to_ip(subnet_mask)
        }
    except Exception as e:
        raise ValueError(f"Error en el cálculo: {str(e)}")

def validate_ip(ip):
    """Valida que la dirección IP tenga un formato correcto."""
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    return all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)
