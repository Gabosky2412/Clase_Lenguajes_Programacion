// hilo principal
// para añadir concurrencia necesitamos añadir hilos, que hay dos formas de agregarlos en java
// 1. implements : Runnable ó 2. extrends : Thread

public class MainClass extends Thread{

	//metodo que se ejecuta por cada instancia del hilo
	public void run() {
		System.out.println(" Ejecutando el hilo "+Thread.currentThread().getId()); //imprime el hilo y numero de este
	}
	
	public static void main(String[] args)
	{
		Account myAccount = new Account(250000);
		
		//1. creacion de dos hilos para las operaciones sobre la cuenta
		Thread hiloRetiro = new Thread( ()-> myAccount.withdraw(100000) );
		Thread hiloDeposito = new Thread( ()-> myAccount.deposit(0) );

		//exageramos y creamos muchos hilos de retiroa la vez para la misma cuenta 
		//es decir que varios hilos invocan el mismo metodo a la vez
		Thread[] hilosRetiro = new Thread[8];

		for(int i = 0; i < hilosRetiro.length; i++){
			hilosRetiro[i] = new Thread( ()-> myAccount.withdraw(100000) );
			hilosRetiro[i].start();
		}

		//2. inicializar hilos
		hiloRetiro.start();
		hiloDeposito.start();

		//3. unir los hilos al hilo principal MAIN
		//e imprimir el id de cada hilo del arreglo de hilos
		try {
			
			// hiloDeposito.join();
			// hiloRetiro.join();

			//inicializamos el arreglo de hilos 
			for(Thread t: hilosRetiro){
				t.join();
				System.out.println("Hilo: "+t.getId());
			}

		} catch (InterruptedException e) {
			
			e.printStackTrace();
		}

		//de aqui en adelante se espera que ambos hilos terminen
		//gracias a que llame a la funcion join en cada uno de ellos

		System.out.println("Balance final: "+myAccount.getBalance());
		// operaciones secuenciales:
		// myAccount.deposit(500000);
		// myAccount.withdraw(40000);
	}

}