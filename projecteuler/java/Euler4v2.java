class Euler4v2 {
	
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
	
	public static int[] problem4(){
		
		int num1 = 1000;
		int num2 = 1000;
		String num_str;
		boolean isPal = false;
		boolean swap = true;
		Integer product = new Integer(0);
		while (!isPal && num1 > 800) {
			num1--;
			num2 = 1000;
			while (!isPal && num2 > 800){
				num2--;
				product = num1 * num2;
				num_str = product.toString();
				isPal = isPalindrome(num_str);
			}
		}
		int[] result = {num1, num2, product};
		return result;
	}
	
	public static void main(String[] args) {
		
		int[] palindrome = problem4();
		StringBuffer output = new StringBuffer();
		for (Integer a : palindrome) {
			output.append(a.toString() + " ");
		}
		System.out.println(output);
	}
}