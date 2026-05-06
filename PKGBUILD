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
sha256sums=('4b541626156638efd8bccb6e341cd409e5cd92d621db799c7cbee1b5161ff44f'
            'ee62a8db740b83ebd4509d0f0fce12efe8d7e180f8c3224116ca012ad9d8d891'
            'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')

package() {
  install -Dm755 "${srcdir}/btrfs-telegram-alert.py" "${pkgdir}/usr/bin/btrfs-telegram-alert"

  install -Dm644 "${srcdir}/config.env.example" "${pkgdir}/etc/btrfs-telegram-notifier/config.env"

  install -Dm644 "${srcdir}/telegram-alert.conf" \
    "${pkgdir}/usr/lib/systemd/system/btrfs-scrub.service.d/telegram-alert.conf"
}
