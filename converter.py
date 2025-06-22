import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Set up argparse
parser = argparse.ArgumentParser(
    description="🌡️ CLI Temperature Converter: Celsius ↔ Fahrenheit"
)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--c2f', type=float, help='Convert Celsius to Fahrenheit')
group.add_argument('--f2c', type=float, help='Convert Fahrenheit to Celsius')

args = parser.parse_args()

# Logic
if args.c2f is not None:
    f = celsius_to_fahrenheit(args.c2f)
    print(f"✅ {args.c2f}°C = {f:.2f}°F")

elif args.f2c is not None:
    c = fahrenheit_to_celsius(args.f2c)
    print(f"✅ {args.f2c}°F = {c:.2f}°C")
