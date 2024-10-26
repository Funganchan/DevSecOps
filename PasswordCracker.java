import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class PasswordCracker {

    // Хэш-значения для проверки
    private static final String[] HASHES = {
            "1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad",
            "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b",
            "74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f",
            "7a68f09bd992671bb3b19a5e70b7827e"
    };

    private static final char[] CHARSET = "abcdefghijklmnopqrstuvwxyz".toCharArray();
    private static final int PASSWORD_LENGTH = 5;

    public static void main(String[] args) throws InterruptedException {
        long startTime = System.currentTimeMillis();
        // Отметка времени для однопоточной обработки
        crackPasswords(1);
        long endTime = System.currentTimeMillis();
        System.out.println("Время выполнения (однопоточный): " + (endTime - startTime) + " мс");
        
        startTime = System.currentTimeMillis();
        // Отметка времени для многопоточной обработки
        crackPasswords(4); // Пример: 4 потока
        endTime = System.currentTimeMillis();
        System.out.println("Время выполнения (многопоточный): " + (endTime - startTime) + " мс");
    }

    private static void crackPasswords(int threadCount) throws InterruptedException {
        ExecutorService executor = Executors.newFixedThreadPool(threadCount);
        
        for (int i = 0; i < Math.pow(CHARSET.length, PASSWORD_LENGTH); i++) {
            final int index = i;
            executor.submit(() -> {
                String password = generatePassword(index);
                String md5Hash = calculateHash(password, "MD5");
                String sha256Hash = calculateHash(password, "SHA-256");
                
                for (String hash : HASHES) {
                    if (md5Hash.equals(hash) || sha256Hash.equals(hash)) {
                        System.out.println("Найден пароль: " + password + " для хэша: " + hash);
                    }
                }
            });
        }
        
        executor.shutdown();
        executor.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
    }

    private static String generatePassword(int index) {
        StringBuilder password = new StringBuilder();
        for (int i = 0; i < PASSWORD_LENGTH; i++) {
            password.append(CHARSET[(index / (int)Math.pow(CHARSET.length, i)) % CHARSET.length]);
        }
        return password.toString();
    }

    private static String calculateHash(String input, String algorithm) {
        try {
            MessageDigest digest = MessageDigest.getInstance(algorithm);
            byte[] hashBytes = digest.digest(input.getBytes());
            StringBuilder hashString = new StringBuilder();
            for (byte b : hashBytes) {
                hashString.append(String.format("%02x", b));
            }
            return hashString.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Алгоритм хеширования не найден", e);
        }
    }
}
