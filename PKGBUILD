# Mantainer: Diego Quarantani <diego.q@ik.me>
pkgname=btrfs-telegram-notifier
pkgver=0.1
pkgrel=1
pkgdesc="Telegram alerts for btrfs scrub failures (btrfsmaintenance integration)"
arch=('any')
url="https://github.com/CetrioloRiick/btrfs-scrub-allert"
license=('GPL')

depends=('python-requests' 'python-dotenv' 'btrfsmaintenance')
source=('btrfs-telegram-alert.py'
        'telegram-alert.conf'
        'config.env.example')
sha256sums=('0a8d0e2a7ff8d90fdfc3f18fd436c99a8a00df0b7ee60a43a00011f064af8614'
            'df60a2c0c76f44dda29f2a47ca0135e55af16a2290d417d9c0d9a0f495702113')

package() {
  install -Dm755 "${srcdir}/btrfs-telegram-alert.py" "${pkgdir}/usr/bin/btrfs-telegram-alert"

  install -Dm644 "${srcdir}/config.env.example" "${pkgdir}/etc/btrfs-telegram-notifier/config.env"

  install -Dm644 "${srcdir}/telegram-alert.conf" \
    "${pkgdir}/usr/lib/systemd/system/btrfs-scrub.service.d/telegram-alert.conf"
}
