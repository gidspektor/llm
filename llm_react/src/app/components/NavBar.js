import Link from 'next/link';
import styles from '@/app/components/NavBar.module.css';

const Navbar = () => {
  return (
    <nav className={styles.navbar}>
      <ul className={styles.navList}>
        <li><Link href="/">Home</Link></li>
        <li><Link href="/create">Create An Article</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
