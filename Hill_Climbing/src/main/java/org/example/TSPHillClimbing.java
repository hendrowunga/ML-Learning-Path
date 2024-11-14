package org.example;

import javax.swing.*;
import java.awt.*;
import java.util.*;

public class TSPHillClimbing extends JFrame {
    private static final int WIDTH = 800;
    private static final int HEIGHT = 600;
    private static final int CITY_RADIUS = 20;
    private static final int NUM_CITIES = 10;

    private ArrayList<City> cities;
    private ArrayList<Integer> currentPath;
    private ArrayList<Integer> bestPath;
    private double bestDistance;

    // Inner class untuk merepresentasikan kota
    private static class City {
        Point location;
        String name;

        City(Point location, String name) {
            this.location = location;
            this.name = name;
        }

        double distanceTo(City other) {
            return location.distance(other.location);
        }
    }

    public TSPHillClimbing() {
        setTitle("TSP Hill Climbing - Indonesia Cities");
        setSize(WIDTH, HEIGHT);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Inisialisasi dengan kota-kota di Indonesia
        initializeIndonesianCities();

        // Inisialisasi jalur awal (random)
        currentPath = new ArrayList<>();
        for (int i = 0; i < cities.size(); i++) {
            currentPath.add(i);
        }
        Collections.shuffle(currentPath);

        bestPath = new ArrayList<>(currentPath);
        bestDistance = calculateTotalDistance(currentPath);

        // Jalankan algoritma Hill Climbing
        hillClimbing();
    }

    private void initializeIndonesianCities() {
        cities = new ArrayList<>();

        // Daftar kota-kota di Indonesia dengan koordinat relatif
        cities.add(new City(new Point(100, 100), "Jakarta"));
        cities.add(new City(new Point(200, 150), "Surabaya"));
        cities.add(new City(new Point(300, 200), "Medan"));
        cities.add(new City(new Point(400, 250), "Bandung"));
        cities.add(new City(new Point(500, 300), "Semarang"));
        cities.add(new City(new Point(150, 350), "Makassar"));
        cities.add(new City(new Point(250, 400), "Palembang"));
        cities.add(new City(new Point(350, 150), "Manado"));
        cities.add(new City(new Point(450, 200), "Yogyakarta"));
        cities.add(new City(new Point(550, 250), "Denpasar"));
    }

    private double calculateTotalDistance(ArrayList<Integer> path) {
        double totalDistance = 0;
        for (int i = 0; i < path.size() - 1; i++) {
            City city1 = cities.get(path.get(i));
            City city2 = cities.get(path.get(i + 1));
            totalDistance += city1.distanceTo(city2);
        }
        // Tambahkan jarak kembali ke kota awal
        totalDistance += cities.get(path.get(path.size() - 1))
                .distanceTo(cities.get(path.get(0)));
        return totalDistance;
    }

    private void hillClimbing() {
        boolean improved;
        do {
            improved = false;

            // Coba semua kemungkinan pertukaran antar dua kota
            for (int i = 0; i < cities.size() - 1; i++) {
                for (int j = i + 1; j < cities.size(); j++) {
                    ArrayList<Integer> newPath = new ArrayList<>(currentPath);
                    // Tukar posisi dua kota
                    Collections.swap(newPath, i, j);

                    double newDistance = calculateTotalDistance(newPath);

                    // Jika mendapatkan jalur yang lebih baik
                    if (newDistance < bestDistance) {
                        bestDistance = newDistance;
                        bestPath = new ArrayList<>(newPath);
                        currentPath = newPath;
                        improved = true;
                        repaint(); // Update visualisasi setiap ada perbaikan
                    }
                }
            }
        } while (improved);
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        // Gambar rute
        g2d.setColor(Color.BLUE);
        g2d.setStroke(new BasicStroke(2));
        for (int i = 0; i < bestPath.size() - 1; i++) {
            City city1 = cities.get(bestPath.get(i));
            City city2 = cities.get(bestPath.get(i + 1));
            g2d.drawLine(city1.location.x, city1.location.y,
                    city2.location.x, city2.location.y);
        }
        // Gambar garis dari kota terakhir ke kota pertama
        City firstCity = cities.get(bestPath.get(0));
        City lastCity = cities.get(bestPath.get(bestPath.size() - 1));
        g2d.drawLine(lastCity.location.x, lastCity.location.y,
                firstCity.location.x, firstCity.location.y);

        // Gambar kota-kota
        for (City city : cities) {
            // Gambar lingkaran untuk kota
            g2d.setColor(Color.WHITE);
            g2d.fillOval(city.location.x - CITY_RADIUS,
                    city.location.y - CITY_RADIUS,
                    CITY_RADIUS * 2, CITY_RADIUS * 2);

            g2d.setColor(Color.RED);
            g2d.drawOval(city.location.x - CITY_RADIUS,
                    city.location.y - CITY_RADIUS,
                    CITY_RADIUS * 2, CITY_RADIUS * 2);

            // Gambar nama kota
            g2d.setColor(Color.BLACK);
            FontMetrics fm = g2d.getFontMetrics();
            int textWidth = fm.stringWidth(city.name);
            int textHeight = fm.getHeight();
            g2d.drawString(city.name,
                    city.location.x - textWidth/2,
                    city.location.y + textHeight/2);
        }

        // Tampilkan jarak total
        g2d.setColor(Color.BLACK);
        g2d.setFont(new Font("Arial", Font.BOLD, 14));
        g2d.drawString("Total Jarak: " + String.format("%.2f", bestDistance) + " unit",
                10, 30);

        // Tampilkan urutan kota
        StringBuilder path = new StringBuilder("Rute: ");
        for (int i = 0; i < bestPath.size(); i++) {
            path.append(cities.get(bestPath.get(i)).name);
            if (i < bestPath.size() - 1) {
                path.append(" → ");
            }
        }
        path.append(" → ").append(cities.get(bestPath.get(0)).name);
        g2d.drawString(path.toString(), 10, 50);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            TSPHillClimbing frame = new TSPHillClimbing();
            frame.setVisible(true);
        });
    }
}