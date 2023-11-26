package PreParcial;

public class Mesero {
    private int cantidadPedidos = 0;
    private final Object lock = new Object();

    public void realizarPedido(String nombrePlato, int cantidad) {
        synchronized (lock) {
            if (cantidadPedidos < cantidad) {
                System.out.println("Mesero: No hay suficientes platos de " + nombrePlato + ". Esperando...");
                try {
                    lock.wait(); // El mesero espera hasta que haya suficientes platos
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            cantidadPedidos -= cantidad;
            System.out.println("Mesero entregó " + cantidad + " platos de " + nombrePlato + ". Pendientes: " + cantidadPedidos);
        }
    }

    public void recibirPedido(int cantidad) {
        synchronized (lock) {
            cantidadPedidos += cantidad;
            System.out.println("Mesero recibió un pedido de " + cantidad + " platos. Pendientes: " + cantidadPedidos);
            lock.notifyAll(); // Notificar a los meseros que están esperando
        }
    }
}