package PreParcial;

public class SimulacionHilos {
    public static void main(String[] args) {

        //llamado a las otras clases por medio de elementos
        Chef chef = new Chef();
        Mesero mesero = new Mesero();

        // Hilos productores (Chefs)
        Thread chef1 = new Thread(() -> chef.producirPlato("Pizza", 5));
        Thread chef2 = new Thread(() -> chef.producirPlato("Pasta", 3));

        // Hilos consumidores (Meseros)
        Thread mesero1 = new Thread(() -> mesero.realizarPedido("Pizza", 2));
        Thread mesero2 = new Thread(() -> mesero.realizarPedido("Pasta", 4));

        // Iniciar los hilos
        chef1.start();
        chef2.start();
        mesero1.start();
        mesero2.start();

        // Esperar a que todos los hilos terminen
        try {
            chef1.join();
            chef2.join();
            mesero1.join();
            mesero2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}