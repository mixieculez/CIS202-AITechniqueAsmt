# Program Developer Name: Michael Boyer
#
# Date Program Developed: 04/11/2025
#
# Organization: CIS 202 - 302
#
# Take two speeches of US President Ronald Reagan. Parse them for all two
# adjacent letter combinations, ignoring all spaces, special characters, and
# numbers. Summarize the number of times each pair is used, and print each
# combination of letters with the number of times it was used.
# The following data structures must be used once:
# 1. List
# 2. Dictionary
# 3. Set
# Output must look professional. `break` and `continue` statements are
# prohibited.
#
# Document your givens below this line
# - Two text files containing speeches by US President Ronald Reagan:
#   1. `eureka_college_1982.txt`
#   2. `unga_1984.txt`
# - We need to analyze letter pairs in these speeches
# - We must use a list, dictionary, and set in our implementation
# - We cannot use `break` or `continue`
#
# Document your inputs below this line
# - Text files containing Reagan's speeches
# - Each file is read as a string and processed for analysis
#
# Document your outputs below this line
# - A formatted analysis of letter pair occurrences for each speech including:
#   - Header with filename
#   - Columns showing each letter pair and its occurrence count
#   - Summary statistics (total pairs and unique pairs)
#
# Document your processes below this line
# 1. Read and parse speech text files
# 2. Extract letter pairs by taking adjacent letters in the cleaned text
# 3. Create a list of all letter pairs
# 4. Use a set to identify unique letter pairs
# 5. Use a dictionary to count occurrences of each pair
# 6. Display formatted results sorted alphabetically by pair
#       - Save formatted results to a .csv file
#
# Start your program code after this line
import os
import csv


class SpeechParser():
    def __init__(self, speech_file):
        # Convert the string with the relative path of the file into a path object
        self.speech_file = os.path.abspath(speech_file)

    def process_speech(self):
        # `parse_to_list` reads the speech file, removes non-alphabetic characters,
        # converts text to lowercase, and creates a list of adjacent letter pairs
        pairs_list = self.parse_to_list()

        # We take the list of pairs and convert it to a set
        # Sets only contain unique elements
        # For example, if our list has ["aa", "aa"], the set will only have one "aa"
        unique_pairs = self.keep_unique_pairs(pairs_list)

        # Create a dictionary where each unique letter pair (from our set) is a key
        # with an initial count of 0. Then iterate through all pairs in the list
        # and increment the counter for each occurrence of that pair.
        pair_counts = self.tally_pairs(pairs_list, unique_pairs)

        # And then print the results (and save them as files)
        self.save_results(pair_counts)

    def parse_to_list(self):
        # Open and read the file in read mode
        with open(self.speech_file, "r") as file:
            text = file.read()

        # Clean text by keeping only letters and converting to lowercase
        cleaned = ''.join(char.lower() for char in text if char.isalpha())

        # Create pairs of adjacent letters until the end of the text,
        # stopping at the second-to-last letter to avoid index errors
        pairs = []
        for i in range(len(cleaned)-1):
            pairs.append(cleaned[i]+cleaned[i+1])

        # Return the list for the next step
        return pairs

    def keep_unique_pairs(self, _list):
        # Convert list to set to get unique pairs
        return set(_list)

    def tally_pairs(self, _list, _set):
        # iterate per element in the set
        # and give it a value of 0 as a key in the
        # new dictionary
        pair_counts = {pair: 0 for pair in _set}

        # Iterate through original list,
        # do the tallying on the dictionary
        for pair in _list:
            pair_counts[pair] += 1

        return pair_counts

    def save_results(self, _dict):
        # Extract the filename from the path for the header
        filename = os.path.basename(self.speech_file)
        base_filename = os.path.splitext(filename)[0]

        # Print header
        print(f"\n{'=' * 50}")
        print(f"LETTER PAIR ANALYSIS FOR: {filename}")
        print(f"{'=' * 50}")

        # Print column headers
        print(f"\n{'PAIR':<10}{'OCCURRENCES':<15}")
        print(f"{'-' * 25}")

        # Print each pair and its count, sorted alphabetically by pair
        for pair in sorted(_dict.keys()):
            print(f"{pair:<10}{_dict[pair]:<15}")

        # Print summary
        total_pairs = sum(_dict.values())
        unique_pairs = len(_dict)
        print(f"\n{'-' * 50}")
        print(f"Total pairs: {total_pairs}")
        print(f"Unique pairs: {unique_pairs}")
        print(f"{'=' * 50}\n")

        # Save results to CSV file
        csv_filename = f"{base_filename}_letter_pairs.csv"

        print(f"Saving results to {csv_filename}...")

        with open(csv_filename, 'w', newline='') as csvfile:
            # Create CSV writer
            csv_writer = csv.writer(csvfile)

            # Write header row
            csv_writer.writerow(['PAIR', 'OCCURRENCES'])

            # Write data rows sorted alphabetically by pair
            for pair in sorted(_dict.keys()):
                csv_writer.writerow([pair, _dict[pair]])

        print(f"CSV file created successfully: {csv_filename}")


if __name__ == "__main__":
    parser_eureka = SpeechParser("extra/eureka_college_1982.txt")
    parser_eureka.process_speech()
    parser_unga = SpeechParser("extra/unga_1984.txt")
    parser_unga.process_speech()

# This is the end of the program
