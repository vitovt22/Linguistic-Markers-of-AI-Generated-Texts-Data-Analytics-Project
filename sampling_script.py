import random
# Insert Python list for sampling
sampling_list = []

# Set random seed for reproducibility
random.seed(42)

# Set sample size required
sample_size = 60

sample = random.sample(sampling_list, sample_size)
print(sample)
