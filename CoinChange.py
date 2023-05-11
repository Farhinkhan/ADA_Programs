# Dynamic Programming Python implementation of Coin Change problem


def count(coins, n, sum):
	# We need sum+1 rows as the table is constructed
	# in bottom up manner using the base case 0 value
	# case (sum = 0)
	table = [[0 for x in range(n)] for x in range(sum+1)]

	# Fill the entries for 0 value case (n = 0)
	for i in range(n):
		table[0][i] = 1

	# Fill rest of the table entries in bottom up manner
	for i in range(1, sum+1):
		for j in range(n):

			# Count of solutions including coins[j]
			x = table[i - coins[j]][j] if i-coins[j] >= 0 else 0

			# Count of solutions excluding coins[j]
			y = table[i][j-1] if j >= 1 else 0

			# total count
			table[i][j] = x + y

	return table[sum][n-1]



if __name__ == '__main__':
	coins = [1, 2, 3]
	n = len(coins)
	sum = 4
	print(count(coins, n, sum))


