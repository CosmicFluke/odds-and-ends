class Euler4 {
	
	private static boolean isPalindrome(String nummy) {

		if (nummy.length() < 2) {
			
			return true;
		}
		
		if (nummy.length() == 2 && nummy.charAt(0) == nummy.charAt(1)){
			return true;
		}
		
		if (nummy.length() == 3 && nummy.charAt(0) == nummy.charAt(2)){
			return true;
		}

		if (nummy.endsWith(String.valueOf(nummy.charAt(0)))) {
			
			return isPalindrome(nummy.substring(1, nummy.length() - 1));
		}

		return false;
		
	}
	
	public static int problem4(){
		
		int num1 = 999;
		int num2 = 999;
		String num_str;
		boolean isPal = false;
		boolean swap = true;
		Integer product = new Integer(0);
		while (!isPal) {
			product = num1 * num2;
			num_str = product.toString();
			isPal = isPalindrome(num_str);
			if (swap) {
				num1--;
			}
			else {
				num2--;
			}
			swap = !swap;
		}
		return product;
	}
	
	public static void main(String[] args) {
		
		int palindrome = problem4();
		System.out.println(palindrome);
	}
}