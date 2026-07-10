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
            jugador.getInventory().add(new ItemStack(Items.valueOf("minecraft:diamond"), 1))
;
            jugador.sendMessage(new StringTextComponent("¡Has recibido un diamante!"), Util.NIL_UUID)
;
        }
    }
    
    public static void teleportHome(Player jugador) {
        // Esto funciona en cualquier versión
        double x = 0.0;
        double y = 70.0;
        double z = 0.0;
        jugador.teleport(new Location(jugador.getCommandSenderWorld(), x, y, z))
;
        jugador.sendMessage(new StringTextComponent("Teletransportado al spawn!"), Util.NIL_UUID)
;
    }
    
    public static void clearAndNotify(Player jugador) {
        jugador.getInventory().clear()
;
        jugador.sendMessage(new StringTextComponent("Inventario limpiado."), Util.NIL_UUID)
;
    }
}
