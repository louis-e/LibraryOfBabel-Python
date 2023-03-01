import random, string, os

charset = 'abcdefghijklmnopqrstuvwxyz, .'
charset_length = len(charset)
max_page_content_length = 3200
max_walls = 4
max_shelves = 5
max_volumes = 32
max_pages = 410
wall = str(random.randint(1, max_walls))
shelf = str(random.randint(1, max_shelves))
volume = str(random.randint(1, max_volumes)).zfill(2)
page = str(random.randint(1, max_pages)).zfill(3)
library_coordinate = int(page + volume + shelf + wall)
hexagon_base = 36

def searchByContent(text, library_coordinate):
    text = ''.join([c for c in text.lower() if c in charset])
    text = text.rstrip().ljust(max_page_content_length, ' ')
    sum_value = 0
    for i, c in enumerate(text[::-1]):
        char_value = ord(c) - ord('a') if c.isalpha() else 28 if c == '.' else 27
        sum_value += char_value * (charset_length**i)

    result = library_coordinate * (charset_length**max_page_content_length) + sum_value
    result = convertToBase(result, hexagon_base)
    return result

def searchByAddress(address):
    hexagon_address, wall, shelf, volume, page = address.split(':')
    volume = volume.zfill(2)
    page = page.zfill(3)
    library_coordinate = int(page + volume + shelf + wall)

    seed = int(hexagon_address, hexagon_base) - library_coordinate * (charset_length**max_page_content_length)
    hexagon_base_result = convertToBase(seed, hexagon_base)
    result = convertToBase(int(hexagon_base_result, hexagon_base), charset_length)

    if len(result) < max_page_content_length:
        random.seed(result)
        while len(result) < max_page_content_length:
            result += charset[int(random.random() * len(charset))]
    elif len(result) > max_page_content_length:
        result = result[-max_page_content_length:]
    return result

def convertToBase(x, base):
    if base == 36: digs = string.digits + 'abcdefghijklmnopqrstuvwxyz'
    elif base == 10: digs = '0123456789'
    elif base == 60: digs = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    else: digs = charset

    if x < 0: sign = -1
    elif x == 0: return digs[0]
    else: sign = 1

    x *= sign
    chars = []
    while x:
        chars.append(digs[x % base])
        x //= base
    if sign < 0:
        chars.append('-')
    chars.reverse()
    return ''.join(chars)


#Page content to hexagon address example
search_term = 'lorem ipsum dolor sit amet'
hexagon_address = searchByContent(search_term, library_coordinate)
total_address = hexagon_address + ':' + wall + ':' + shelf + ':' + volume + ':' + page
print("Hexagon address:", total_address)

#Hexagon address to page content example
example_address = '1hhghb34c6mgty6igk9r8i96rupztwalyfia8c5v909vxdpqprn9z56kefhfm0d72bssm8kc7sgvtit0c4l8h583jee52tl23khmt7z9vtfxn8rwgf411t726qi4s9sk98jlm1euuv3689gm608ualkwnqezr92y8ae405qm7qib35qfnloc4aj5a07a4kmiwll1cwb6jaaouacvuoy7oa8yk1bgil7rjp9r3revufqonix87kdv017y71abs4q3ljtulfml7nr7705qefufoti9cvgg52h0i5w4engod6bxovb6r0zupxne6wgmlp2hsw4j8vyruywyd4zdvt3kx9hnvqf6d14j03an9ropg4li8ox1rlv2ip1te89acpjpc3wnqv6e638ctlyu2iz8ofvrf5tku5p1ywu0u50ktd1oxivh97uo9x0kl5sxhgvgalhjz2fvlj4jx36keehokptxy39prjtegupr1ygv9pex5o9od9t194nnlroq89edsdsw29pdevi56js579xcv9m5w59ag2iki4477yj4yi64fhzl6n8trscrjvti06unk5rnm61uoqd0t1ak299sl59j3jag8s01scoeauo4be94h9s3gk39y1ggsymyh4tlp7uokv4n34dvfdti0pvlaoencdjzrwuf7gcoio9bc99cbos4swokwct27wwwluvm4k4itimxwfi70fn96xcejhexccfknkf1j2jlpgn3m4nr2sqmjspl2h47o9hjtacppizraeq9gwfd1nu9vl2m2b40et5lxqn7121mjlm4lllplroboqxy0kp0fpknt78npgwp5gz3jqrpyvcoffwkr30tb3293xpiqpf5apb4f3udnqr5orvosu4e35pxiouuvabnhcjcqkv043bdb04dot7daqmjpnyhe6cjvm55lhqqjh9vahmnaxuakldecc0v6hiecjwujniy7tz1b06crh5b9gsg8zf6calun0e20ubkr5e6grls67sb2gms1dz5mhedtpyxdwyct8authhui7vlkqpqlvjce6iuq32oeh5pz4gblnfnk9s6ciqa2ifkpl20t50g5w7q7gkzh6u0q360yedkrdcwvdvy13sywa9bv9gkxsn2ai3ohjfjiwp97kabo17wy2pabcz24u1qrmoa61nvn9irfpjblf1tw7w49os85b86jhr0h42hb7oqr0ux02nu2kpma8vj3mbw3jnlhd0qfc5qmxguxalblm10oxmn5wm5fuijimb5hf9yd4719sx0n42mg36aoifw77z6qc67ft8tojf8fl2l9ysouw7ps9bgm9f2zy0141rw4d0xxlqlanjyvrgvij0136lt9770mf8ftbitwjrqk59j9sl7fy23byp1ykgprwqcu0nukjhu37ffpuz796qggfm9r7rqbr2uxbyjorsqyob79eotcpxbp2zhwm464h9udn38nsfz3ppdspnx5lesdphzoc7rcr97dc0jhxekf3sqvlbcdhkftwyoacn75gg4wnaj51f9vm17nvwbq1gjbh6r72yhv887gqclkkw1tcbqiqjqus0w79r5fkhjla7zezsfoex86sgmkw9x62k6qsr3vdn5pgo157jajhgvp03eewjsqxiokklampfikco46abch7j5cv4zlynsj7mn2yrjmqg34qvh5440nn4z7v4zf5gavz0dorfhtpgcnwx4g5p9u98kyqowkpstz4i7wgqeoggo4sulxu586kjbt2jgccwo4yecx2tq1eavdb61tozw4lpkbp8mme9ca73fpjvh8xvimfj9l57xq4ok0682etbuke9v61v5sw8qxitekgbtvy5hqwvpc5hqit8eaf4ezl7kzjoi489m69ltrl4ya6stebzbi26lzqo6w6xm0i0op1qmi8f77iemgmkoxlsvukbob2bjz1m4aaqprjp0hutwvpnq63nv6f64zy6fmardz8c5ztbj8hlfez9oc709lq0goa1urcs2wwrcveaw81zxzuge0asebvaep7nzlpz6ow57m055zfneugeiz0k8v4lifeb9f6get0v9fh2zxj2mtqmz7n602lsdy316ch5c3h33jp00n1ud9xwr0vlnxm9xalcuzidqhcl2qan9wyl4uga3qj4lftfivo25in79k1fylcw1151c0d18uyh1u198et5bh6q8hruxx2vjyv2idm7ujftrbjzn7u5nqzb3gs1abq561fwc326e0iserz4tawb9ehwfkfrumx6yeydyxhgqsc2t8m8vqoypvogl6zfyowm1h4pgsrrkk3nr2pib7362z74n2fpisyupr9v4xvial36lyijrsuepcfb3rtxgoqhdpvzaq20sq071q3bn54784jw5xji8otoerllhyu13ogciz79imgzq5gi8388qh3g1ygbi8nyu8h6llk3izjn3lbbqvookqiedkx6zjfqaq99n9krfkf6tunn3i8t1mpp9a159zf3ea8ojcayupbdeh0zg30m1iz728ohmvxnuwcddg3st5tbzcgbvnw52nmkio6pi8ztybq4o57nhialc2d86ag41r7qoa8vwhiy0mon60az6wpapwxilu2ezadr25qe9ng1a3d1gckoofu61z3kqfirc2opul1jvnkvpooyjthqx7xsyw0hmfv2kzkx8lakc6pavvbpwwvhone598b78qy5pgo6azqk71r70belus6752sitf9gcj9ws9xgju9vb514mar1advy23v4kp4n7ryupsvmdwyhod79wbafplcifydl2n639y5z8zdk700jfm4srteyndln5giu9lc68r3s309wg4qe2uqjdg4rznhthq0pk8su645bkcwsk4uab9270ngdcc8c4i60xdzgyh0ci3aqsauzh4twb7p4qfu8wxmrq0ax6igqm0akamjq2tfkcbb4zi8vg2z1ylloaypxaczcbvdu1pwx6ockubl05n9ocvqtf:1:3:09:335'
contentByAddress = searchByAddress(total_address)
print("Page content:", contentByAddress.rstrip())
