# Java RandomAccessFile Class
    RandomAccessFile raf = new RandomAccessFile(filepath, "rw");// 这个类可以实现指定位置的读写操作
    raf.seek(30);     //从第三十个字节开始进行io操作
    String content = raf.readLine();  //照常读写