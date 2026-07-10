package net.javacraft.testmod;

// Estos imports serán reemplazados por los de cada versión
import net.minecraft.entity.player.EntityPlayer;

import net.minecraft.world.World;

import net.minecraft.item.ItemStack;

import net.minecraft.util.text.ChatComponentText;

import net.minecraft.entity.player.InventoryPlayer;


public class ModActions {
    
    public static void giveDiamond(Player jugador) {
        // Java puro con macros de Javacraft
        if (jugador.isAlive()) {
            jugador.getInventory().addItem(new ItemStack(Material.getMaterial("minecraft:diamond"), 1))
;
            jugador.sendMessage(new ChatComponentText("¡Has recibido un diamante!"))
;
        }
    }
    
    public static void teleportHome(Player jugador) {
        // Esto funciona en cualquier versión
        double x = 0.0;
        double y = 70.0;
        double z = 0.0;
        jugador.teleport(new Location(jugador.getWorld(), x, y, z))
;
        jugador.sendMessage(new ChatComponentText("Teletransportado al spawn!"))
;
    }
    
    public static void clearAndNotify(Player jugador) {
        jugador.getInventory().clear()
;
        jugador.sendMessage(new ChatComponentText("Inventario limpiado."))
;
    }
}
