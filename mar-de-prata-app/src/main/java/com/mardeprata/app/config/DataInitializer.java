package com.mardeprata.app.config;

import com.mardeprata.app.model.MenuItem;
import com.mardeprata.app.model.RestaurantTable;
import com.mardeprata.app.repository.MenuItemRepository;
import com.mardeprata.app.repository.RestaurantTableRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class DataInitializer implements CommandLineRunner {

    @Autowired
    private MenuItemRepository menuItemRepository;

    @Autowired
    private RestaurantTableRepository tableRepository;

    @Override
    public void run(String... args) throws Exception {
        if (menuItemRepository.count() == 0) {
            int order = 1;

            // ENTRADAS
            save("Amêijoas à Bulhão Pato", "Amêijoas frescas salteadas com azeite, alho e coentros", 8.50, "Entradas", order++, false, false, false, false, false, false, true, false, false, false, false, false, false, true, true, false, false);
            save("Camarão ao Alho", "Camarão tigre salteado em manteiga e alho", 11.00, "Entradas", order++, false, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false);
            save("Percebes", "Percebes frescos cozidos no ponto", 14.00, "Entradas", order++, false, false, false, false, false, false, false, false, false, false, false, false, false, true, false, false, false);
            save("Pataniscas de Bacalhau", "Pataniscas tradicionais de bacalhau com feijão", 7.50, "Entradas", order++, true, false, true, true, false, false, false, false, false, false, false, false, false, false, false, false, false);

            // SOPAS
            save("Caldo Verde", "Sopa tradicional portuguesa com couve, batata e chouriço", 4.50, "Sopas", order++, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, true, false);
            save("Sopa de Marisco", "Creme rico de marisco com tomate e brandy", 7.50, "Sopas", order++, false, true, false, false, false, false, false, false, false, false, false, false, false, true, false, false, false);

            // PRATOS DO MAR
            save("Bacalhau à Brás", "Bacalhau desfiado com ovos mexidos, batata palha e azeitonas", 16.50, "Pratos do Mar", order++, true, false, true, true, false, false, false, false, false, false, false, false, false, false, true, false, false);
            save("Arroz de Lingueirão", "Arroz caldoso com lingueirão fresco e coentros", 19.00, "Pratos do Mar", order++, false, false, false, false, false, false, false, false, false, false, false, false, false, true, false, false, false);
            save("Cataplana de Marisco", "Cataplana tradicional algarvia com marisco variado", 24.50, "Pratos do Mar", order++, false, true, false, false, false, false, false, false, false, false, false, false, false, true, true, false, false);
            save("Polvo à Lagareiro", "Polvo assado no forno com batatas a murro e azeite", 18.50, "Pratos do Mar", order++, false, false, false, false, false, false, false, false, false, false, false, false, false, true, false, false, false);
            save("Açorda de Gambas", "Açorda alentejana com gambas, coentros e pão", 17.00, "Pratos do Mar", order++, true, true, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false);

            // GRELHADOS
            save("Dourada Grelhada", "Dourada fresca grelhada com legumes salteados", 15.50, "Grelhados", order++, false, false, false, true, false, false, false, false, false, false, false, false, false, false, false, false, false);
            save("Robalo no Sal", "Robalo inteiro assado em crosta de sal grosso", 17.00, "Grelhados", order++, false, false, false, true, false, false, false, false, false, false, false, false, false, false, false, false, false);
            save("Entrecôte 300g", "Entrecôte de novilho grelhado com molho bernaise", 18.50, "Grelhados", order++, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false);

            // SOBREMESAS
            save("Pudim Flan", "Pudim flan clássico com calda de caramelo", 4.50, "Sobremesas", order++, true, false, true, false, false, false, true, false, false, false, false, false, false, false, false, false, false);
            save("Mousse de Chocolate", "Mousse de chocolate negro com amendoas tostadas", 5.00, "Sobremesas", order++, false, false, true, false, false, false, true, true, false, false, false, false, false, false, false, false, false);
            save("Arroz Doce", "Arroz doce tradicional polvilhado com canela", 4.00, "Sobremesas", order++, false, false, true, false, false, false, true, false, false, false, false, false, false, false, false, false, false);

            // BEBIDAS
            save("Água", "Água mineral natural ou com gás", 1.50, "Bebidas", order++, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false);
            save("Vinho Verde (garrafa)", "Vinho Verde branco, região do Minho", 12.00, "Bebidas", order++, false, false, false, false, false, false, false, false, false, false, false, true, false, false, false, false, false);
            save("Super Bock", "Cerveja Super Bock nacional (33cl)", 2.50, "Bebidas", order++, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false);
            save("Sumo Natural", "Sumo de laranja espremido na hora", 3.50, "Bebidas", order++, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false);

            System.out.println("✅ DataInitializer: " + menuItemRepository.count() + " pratos inseridos.");
        }

        if (tableRepository.count() == 0) {
            for (int i = 1; i <= 10; i++) {
                RestaurantTable table = new RestaurantTable();
                table.setTableNumber(i);
                table.setActive(true);
                table.setCapacity(4);
                table.setQrCodeUrl("https://api.qrserver.com/v1/create-qr-code/?data=http://76.13.41.197:8083/menu.html%3Ftable=" + i + "&size=150x150");
                tableRepository.save(table);
            }
            System.out.println("✅ DataInitializer: 10 mesas inseridas.");
        }
    }

    private void save(String name, String desc, double price, String category, int order,
                      boolean hasGluten, boolean hasCrustaceans, boolean hasEggs, boolean hasFish,
                      boolean hasPeanuts, boolean hasSoy, boolean hasMilk, boolean hasNuts,
                      boolean hasCelery, boolean hasMustard, boolean hasSeeds, boolean hasSulphites,
                      boolean hasLupin, boolean hasMolluscs, boolean featured,
                      boolean vegetarian, boolean vegan) {
        MenuItem item = new MenuItem();
        item.setName(name);
        item.setDescription(desc);
        item.setPrice(price);
        item.setCategory(category);
        item.setDisplayOrder(order);
        item.setHasGluten(hasGluten);
        item.setHasCrustaceans(hasCrustaceans);
        item.setHasEggs(hasEggs);
        item.setHasFish(hasFish);
        item.setHasPeanuts(hasPeanuts);
        item.setHasSoy(hasSoy);
        item.setHasMilk(hasMilk);
        item.setHasNuts(hasNuts);
        item.setHasCelery(hasCelery);
        item.setHasMustard(hasMustard);
        item.setHasSeeds(hasSeeds);
        item.setHasSulphites(hasSulphites);
        item.setHasLupin(hasLupin);
        item.setHasMolluscs(hasMolluscs);
        item.setFeatured(featured);
        item.setVegetarian(vegetarian);
        item.setVegan(vegan);
        item.setActive(true);
        menuItemRepository.save(item);
    }
}
