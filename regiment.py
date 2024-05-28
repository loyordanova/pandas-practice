# Step 1. Import the necessary libraries
import pandas as pd

# ------------------------------------------------------------------------------------------------

# Step 2. Create the DataFrame with the following values:
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

# ------------------------------------------------------------------------------------------------

# Step 3. Assign it to a variable called regiment.
regiment = pd.DataFrame(raw_data, columns = raw_data.keys())
# print(regiment.head())

# ------------------------------------------------------------------------------------------------

# Step 4. What is the mean preTestScore from the regiment Nighthawks?
mean_preTestScore = regiment[regiment['regiment'] == 'Nighthawks']['preTestScore'].mean()
# print(mean_preTestScore)

# ------------------------------------------------------------------------------------------------

# Step 5. What is the mean preTestScore from the regiment Nighthawks?
# mean_preTestScore_nighthawks = regiment[regiment['regiment'] == 'Nighthawks']['preTestScore'].mean()
# print(mean_preTestScore_nighthawks)

# ------------------------------------------------------------------------------------------------

# Step 6. Present general statistics by company
# general_statistics = regiment.groupby('company').describe()
# print(general_statistics)

# ------------------------------------------------------------------------------------------------

# Step 7. What is the mean of each company's preTestScore?'
# mean_preTestScore_per_company = regiment.groupby('company')['preTestScore'].mean()
# print(mean_preTestScore_per_company)

# ------------------------------------------------------------------------------------------------

# Step 8. Present the mean preTestScores grouped by regiment and company
# groupedByPreTestScore = regiment.groupby(['regiment', 'company'])['preTestScore'].mean()
# print(groupedByPreTestScore)

# ------------------------------------------------------------------------------------------------