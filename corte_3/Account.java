public class Account {
	
	private float balance;
	
	
	public Account(float initialBalance)
	{
		this.balance = initialBalance;
	}

    public float getBalance() {
        return balance;
    }
	
	/**
	 * retiro. Metodo sincronizado, con el "synchronized" quiere decir que solo un hilo puede usar dicho metodo,
     * //si se llega a usar el metodo desde dos hilos diferentes se creara una cola de espera 
	 * @param amount
	 */
	public synchronized void withdraw(float amount)
	{
		//validar balance >= valor a retirar
		if (balance >= amount) {
            balance -= amount;
        }else {
            System.out.println("el retiro supera el balance");
        }
	}
	
	/**
	 * depósito
	 * @param amount
	 */
	public void deposit(float amount)
	{
		balance += amount;
	}

}