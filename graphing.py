import pandas as pd
import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv('IR2.csv')  

def plot_compound(data, compound, color, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Wavenumber'], data[compound], color=color)
    plt.gca().invert_xaxis()  
    plt.xlabel('Wavenumber (cm⁻¹)')
    plt.ylabel('Transmittance (%)')
    plt.title(title)
    plt.gca().xaxis.tick_top()  
    plt.gca().xaxis.set_label_position('top')  
    plt.grid(False)  
    plt.savefig(f"{title.replace(' ', '_')}.png")  
    plt.show()


plot_compound(data, 'Bromobenzene', 'green', 'IR Spectrum of Bromobenzene')
#plot_compound(data, 'Benzoic Acid', 'blue', 'IR Spectrum of Benzoic Acid')
#plot_compound(data, 'Ethyl Benzoate', 'red', 'IR Spectrum of Ethyl Benzoate')
