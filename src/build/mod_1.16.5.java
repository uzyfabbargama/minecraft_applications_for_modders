package net.javacraft.testmod;

// Estos imports serán reemplazados por los de cada versión
IMPORT_PLAYER
IMPORT_WORLD
IMPORT_ITEM
IMPORT_CHAT
IMPORT_INVENTORY

public class ModActions {
    
    public static void giveDiamond(Player jugador) {
        // Java puro con macros de Javacraft
        if (jugador.isAlive()) {
            jugador.getInventory().add(new ItemStack(Registry.ITEM.get(new ResourceLocation("minecraft:diamond")), 1))
;
            jugador.sendMessage(Component.literal("¡Has recibido un diamante!"), Util.NIL_UUID)
;
        }
    }
    
    public static void teleportHome(Player jugador) {
        // Esto funciona en cualquier versión
        double x = 0.0;
        double y = 70.0;
        double z = 0.0;
        jugador.teleport(new Location(jugador.getLevel(), x, y, z))
;
        jugador.sendMessage(Component.literal("Teletransportado al spawn!"), Util.NIL_UUID)
;
    }
    
    public static void clearAndNotify(Player jugador) {
        jugador.getInventory().clear()
;
        jugador.sendMessage(Component.literal("Inventario limpiado."), Util.NIL_UUID)
;
    }
}
