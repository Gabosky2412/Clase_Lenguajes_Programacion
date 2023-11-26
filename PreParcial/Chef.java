package PreParcial;

public class Chef {
    private int cantidadPlatos = 0;
    private final Object lock = new Object();

    public void producirPlato(String nombrePlato, int cantidad) {
        synchronized (lock) {
            cantidadPlatos += cantidad;
            System.out.println("Chef produjo " + cantidad + " platos de " + nombrePlato + ". Total: " + cantidadPlatos);
        }
    }
}