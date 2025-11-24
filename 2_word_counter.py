import re

def read_text_from_file(filename):
    """
    Reads text content from a file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return ""

def count_word_frequency(text):
    """
    Counts frequency of each word in the text using a dictionary
    """
    # Convert to lowercase and extract words (letters only)
    words = re.findall(r'\b[a-z]+\b', text.lower())
    
    # Count frequencies using dictionary
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

def display_top_words(frequency, top_n=10):
    """
    Displays the top N most frequent words
    """
    # Sort by frequency in descending order
    sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    print("\n" + "="*60)
    print(f" Top {top_n} Most Frequent Words")
    print("="*60)
    
    for idx, (word, count) in enumerate(sorted_words[:top_n], 1):
        print(f"{idx:2}. {word:20} : {count:3} times")
    
    print("-"*60)
    print(f"Total Unique Words: {len(frequency)}")
    print(f"Total Words: {sum(frequency.values())}")
    print("="*60)

def save_frequency_report(frequency, output_file):
    """
    Saves word frequency analysis to a file
    """
    sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Word Frequency Analysis Report\n")
        file.write("Author: K Premila Singha\n")
        file.write("="*60 + "\n\n")
        
        file.write(f"{'Word':<20} {'Frequency':>10}\n")
        file.write("-"*60 + "\n")
        
        for word, count in sorted_words:
            file.write(f"{word:<20} {count:>10}\n")
        
        file.write("\n" + "="*60 + "\n")
        file.write(f"Total Unique Words: {len(frequency)}\n")
        file.write(f"Total Words: {sum(frequency.values())}\n")
    
    print(f"\n✓ Full report saved to '{output_file}'")

def main():
    """
    Main function to orchestrate the program
    """
    print("\n Word Frequency Counter")
    print("Author: K Premila Singha\n")
    
    input_file = "input_files/book.txt"
    output_file = "output_files/word_frequency.txt"
    
    # Read text from file
    text = read_text_from_file(input_file)
    
    if not text:
        return
    
    print(f"✓ Text loaded from '{input_file}'")
    
    # Count word frequencies
    frequency = count_word_frequency(text)
    
    # Display top words
    display_top_words(frequency, top_n=15)
    
    # Save full report
    save_frequency_report(frequency, output_file)

if __name__ == "__main__":
    main()