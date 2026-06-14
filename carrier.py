import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type

def get_phone(num_str):
    try:
        parsed = phonenumbers.parse(num_str)

        if not phonenumbers.is_valid_number(parsed):
            return {"error": "Invalid number"}

        num_type = number_type(parsed)

        # Convert number type to readable text
        if num_type == phonenumbers.PhoneNumberType.MOBILE:
            type_name = "Mobile"
        elif num_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            type_name = "Landline"
        elif num_type == phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE:
            type_name = "Fixed line or Mobile"
        elif num_type == phonenumbers.PhoneNumberType.VOIP:
            type_name = "VoIP"
        elif num_type == phonenumbers.PhoneNumberType.TOLL_FREE:
            type_name = "Toll-free"
        else:
            type_name = "Unknown"

        return {
            "type": type_name,
            "location": geocoder.description_for_number(parsed, "en"),
            "carrier": carrier.name_for_number(parsed, "en"),
            "timezones": timezone.time_zones_for_number(parsed)
        }

    except Exception as e:
        return {"error": str(e)}

info = get_phone("+91")
print(info)

