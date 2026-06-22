import os

class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, item):
        self.stack.append(item)
        if not self.max_stack:
            self.max_stack.append(item)
        else:
            current_max = max(item, self.max_stack[-1])
            self.max_stack.append(current_max)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow: Cannot pop from an empty stack.")
        self.max_stack.pop()
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty: Cannot peek.")
        return self.stack[-1]

    def get_max(self):
        if self.is_empty():
            return 0  
        return self.max_stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

def find_river_view_buildings(heights):
    if not heights:
        return []

    max_stack = MaxStack()
    result = []

    # Process from RIGHT to LEFT
    for i in range(len(heights) - 1, -1, -1):
        # Get maximum height to the right of current building
        max_right = max_stack.get_max()
        
        # If current building is taller than max to its right, it has river view
        if heights[i] > max_right:
            result.append(i)
        
        # Add current building height to the max stack
        max_stack.push(heights[i])

    result.reverse()
    return result

def main():
    try:
        # Get the directory where the script resides
        directory_path = os.path.dirname(os.path.abspath(__file__))

        # Prompt user for file names with defaults
        input_file_name = input("Enter input file name [default: inputPS02.txt]: ").strip()
        output_file_name = input("Enter output file name [default: outputPS02.txt]: ").strip()

        # Apply default values if empty
        if not input_file_name:
            input_file_name = 'inputPS02.txt'
        if not output_file_name:
            output_file_name = 'outputPS02.txt'

        input_file_path = os.path.join(directory_path, input_file_name)
        output_file_path = os.path.join(directory_path, output_file_name)

        # Check input file exists
        if not os.path.exists(input_file_path):
            raise FileNotFoundError(f"Input file not found: {input_file_path}")

        # Read and strictly validate input
        with open(input_file_path, 'r') as file:
            line = file.readline().strip()
            if not line:
                raise ValueError("Input file is empty.")

            line = line.replace('[', '').replace(']', '')
            parts = line.split(',')

            heights = []
            for part in parts:
                part = part.strip()
                if not part.isdigit():
                    raise ValueError("Input must contain only non-negative integers, comma-separated.")
                heights.append(int(part))

        # Compute river view buildings
        result = find_river_view_buildings(heights)

        # Write result to output file
        with open(output_file_path, 'w') as file:
            file.write(str(result))

        # Console output
        print(f"\nInput: {heights}")
        print(f"Output (river view indices): {result}")

    except FileNotFoundError as fnf_error:
        print(f"File Error: {fnf_error}")
    except ValueError as val_error:
        print(f"Input Error: {val_error}")
        print(f"Provided input: '{line}'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
