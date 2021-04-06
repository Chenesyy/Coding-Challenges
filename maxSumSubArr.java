import java.util.*;

class maxSumSubArr {
	public static int findMaxSum(int[] arr) {
		int max = arr[0];
		int temp = arr[0];
		
		for (int i=1; i < arr.length; i++) {
			temp = Math.max(arr[i], temp + arr[i]);
			if (temp > max) {
				max = temp;
			}
		}
		return max;
	}
	
	public static void main(String[] args) {
		int[] arr = {-2, 1, -3, 5, -1, 2, 1, -5, 4};
		
		System.out.print(findMaxSum(arr));
	}
}

//Used Kadane's Algorithm (DP)