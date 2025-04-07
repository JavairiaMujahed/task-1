# task-1
elevate labs data analyst internship task 1
<br/>
<p>
Handling Missing Values:
I identified missing values in several columns using isna() and isnull().
I initially tried replacing missing values with 0 using fillna(value=0).
Later, I used forward fill (fillna(method='ffill')) to fill missing values with the previous valid entry in the column.
Finally, I replaced missing values in 'genre2' and 'genre3' columns with the string "Unknown".
</p>
<br/>
<p>
Dropping Columns:
I removed the 'director' and 'cast' columns as they were deemed unnecessary for my analysis.
I dropped the original 'duration' column after converting the duration values to minutes and storing it in a new column called duration_numeric.
The original 'genre' column was removed after splitting its contents into 'genre1', 'genre2', and 'genre3' columns.
</p>
<br/>
<p>
  Data Type Conversion:
I converted the 'date_added' column to datetime format using pd.to_datetime() and then to 'dd-mm-yyyy' string format using dt.strftime().
I converted several columns ('type', 'country', 'description', 'genre1', 'genre2', 'genre3') to string type using astype('string').
</p>
  Handling Duplicates:
I checked for duplicate rows using duplicated() and value_counts().
I removed duplicate rows, keeping the first occurrence, using drop_duplicates().
<br/>

Data Transformation:
I split the 'listed_in' column (which I later renamed to 'genre') into three separate columns ('genre1', 'genre2', 'genre3') to handle multiple genres associated with each title.
I converted the 'duration' column, which had mixed units (seasons and minutes), to a consistent unit (minutes) in the new 'duration_numeric' column. I assumed 30 episodes per season and 25 minutes per episode for TV shows.
<br/>
Renaming Columns:
I renamed the 'listed_in' column to 'genre' using rename().
<br/>
Saving the Cleaned Data:
I saved the cleaned dataset to a CSV file named 'cleaned_netflix_data.csv', first in the current working directory and then to my Google Drive in a folder called 'Netflix_Data'.
