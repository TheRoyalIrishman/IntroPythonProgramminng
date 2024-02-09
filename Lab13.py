import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def monteCarloSims(numSims):
    results = []

    for N in range(1, numSims + 1):
        # Perform N random ball tosses into N bins
        bins = np.zeros(N)
        tosses = np.random.randint(0, N, N)
        
        for toss in tosses:
            bins[toss] += 1

        # Count the number of non-empty bins
        fullBins = np.sum(bins > 0)
        results.append(fullBins)

    return results

def main():
    numSims = 1000
    simResults = monteCarloSims(numSims)

    # Plot the results
    plt.plot(range(1, numSims + 1), simResults, 'o', label='Simulation Results')
    
    # Perform linear regression
    slope, intercept, rvalue, _, _ = linregress(range(1, numSims + 1), simResults)

    # Plot the best fit line
    plt.plot(range(1, numSims + 1), intercept + slope * np.array(range(1, numSims + 1)),
              'r',
              label=f'Best Fit Line (slope={slope:.4f}, rvalue={rvalue:.4f})'
            )

    plt.xlabel('Number of Bins (N)')
    plt.ylabel('Number of Non-Empty Bins')
    plt.legend()
    plt.show()

    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    print(f"R2 Value: {rvalue}")

if __name__ == "__main__":
    main()
