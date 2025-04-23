* I use np.set_printoptions to set the precision to 2; otherwise, the output would be too long, like 84.33333333.

* scores.mean() means calculating the average value. The axis is the first parameter of the .mean() function. When it is set to 1, it means calculating by row; when it is set to 0, it means calculating by column.

* scores.sum(axis=1) means calculating the total score by row. The meaning of axis=1 is the same as above.

* np.argmax(total_scores) returns the index of the largest number.

* I use scores.copy() here to avoid editing the raw data in scores. In scores_with_bonus[:, 2] += 5, : means all rows are affected; every element at index 2 of every row will be increased by 5.