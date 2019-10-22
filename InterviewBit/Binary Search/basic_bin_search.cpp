int binarySearch(int *Arr, int n, int target) {

	//set stating and ending index
	int start = 0, ending = n-1;

	while(start <= ending) {
		// take mid of the list
		int mid = (start + end) / 2;

		// we found a match
		if(Arr[mid] == target) {
			return mid;
		}
		// go on right side
		else if(Arr[mid] < target) {
			start = mid + 1;
		}
		// go on left side
		else {
			end = mid - 1;
		}
	}
	// element is not present in list
	return -1;
}
