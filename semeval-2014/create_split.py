import xml.etree.ElementTree as ET
import random

random.seed(1)

def split_xml_data(input_file, train_file, val_file, test_file, val_ratio=0.1, test_ratio=0.1):
    # Parse the XML file
    tree = ET.parse(input_file)
    root = tree.getroot()
    
    # Get all sentences and shuffle them
    sentences = list(root)
    random.shuffle(sentences)
    
    # Calculate split sizes
    total_sentences = len(sentences)
    test_size = int(500)
    val_size = int(500)
    train_size = total_sentences - test_size - val_size
    
    # Create new XML roots for each split
    train_root = ET.Element('sentences')
    val_root = ET.Element('sentences')
    test_root = ET.Element('sentences')
    
    # Split the sentences
    train_sentences = sentences[:train_size]
    val_sentences = sentences[train_size:train_size + val_size]
    test_sentences = sentences[train_size + val_size:]
    
    # Add sentences to respective splits
    for sentence in train_sentences:
        train_root.append(sentence)
    
    for sentence in val_sentences:
        val_root.append(sentence)
    
    for sentence in test_sentences:
        test_root.append(sentence)
    
    # Create new XML trees
    train_tree = ET.ElementTree(train_root)
    val_tree = ET.ElementTree(val_root)
    test_tree = ET.ElementTree(test_root)
    
    # Write to files with proper XML formatting
    train_tree.write(train_file, encoding='utf-8', xml_declaration=True)
    val_tree.write(val_file, encoding='utf-8', xml_declaration=True)
    test_tree.write(test_file, encoding='utf-8', xml_declaration=True)
    
    # Print statistics
    print(f"Total sentences: {total_sentences}")
    print(f"Training set size: {train_size} ({train_size/total_sentences*100:.1f}%)")
    print(f"Validation set size: {val_size} ({val_size/total_sentences*100:.1f}%)")
    print(f"Test set size: {test_size} ({test_size/total_sentences*100:.1f}%)")

# Optional: Set random seed for reproducibility
def set_seed(seed):
    random.seed(seed)

if __name__ == "__main__":
    # Set random seed for reproducibility (optional)
    set_seed(42)
    
    # Define file paths
    input_file = "input.xml"
    train_file = "train.xml"
    val_file = "val.xml"
    test_file = "test.xml"
    
    # Create splits (80/10/10 by default)
    split_xml_data(input_file, train_file, val_file, test_file)
