deps_config := \
	/home/aaronjs/esp/esp-idf/components/app_trace/Kconfig \
	/home/aaronjs/esp/esp-idf/components/aws_iot/Kconfig \
	/home/aaronjs/esp/esp-idf/components/bt/Kconfig \
	/home/aaronjs/esp/esp-idf/components/driver/Kconfig \
	/home/aaronjs/esp/esp-idf/components/efuse/Kconfig \
	/home/aaronjs/esp/esp-idf/components/esp32/Kconfig \
	/home/aaronjs/esp/esp-idf/components/esp_adc_cal/Kconfig \
	/home/aaronjs/esp/esp-idf/components/esp_event/Kconfig \
	/home/aaronjs/esp/esp-idf/components/esp_http_client/Kconfig \
	/home/aaronjs/esp/esp-idf/components/esp_http_server/Kconfig \
	/home/aaronjs/esp/esp-idf/components/esp_https_ota/Kconfig \
	/home/aaronjs/esp/esp-idf/components/espcoredump/Kconfig \
	/home/aaronjs/esp/esp-idf/components/ethernet/Kconfig \
	/home/aaronjs/esp/esp-idf/components/fatfs/Kconfig \
	/home/aaronjs/esp/esp-idf/components/freemodbus/Kconfig \
	/home/aaronjs/esp/esp-idf/components/freertos/Kconfig \
	/home/aaronjs/esp/esp-idf/components/heap/Kconfig \
	/home/aaronjs/esp/esp-idf/components/libsodium/Kconfig \
	/home/aaronjs/esp/esp-idf/components/log/Kconfig \
	/home/aaronjs/esp/esp-idf/components/lwip/Kconfig \
	/home/aaronjs/esp/esp-idf/components/mbedtls/Kconfig \
	/home/aaronjs/esp/esp-idf/components/mdns/Kconfig \
	/home/aaronjs/esp/esp-idf/components/mqtt/Kconfig \
	/home/aaronjs/esp/esp-idf/components/nvs_flash/Kconfig \
	/home/aaronjs/esp/esp-idf/components/openssl/Kconfig \
	/home/aaronjs/esp/esp-idf/components/pthread/Kconfig \
	/home/aaronjs/esp/esp-idf/components/spi_flash/Kconfig \
	/home/aaronjs/esp/esp-idf/components/spiffs/Kconfig \
	/home/aaronjs/esp/esp-idf/components/tcpip_adapter/Kconfig \
	/home/aaronjs/esp/esp-idf/components/unity/Kconfig \
	/home/aaronjs/esp/esp-idf/components/vfs/Kconfig \
	/home/aaronjs/esp/esp-idf/components/wear_levelling/Kconfig \
	/home/aaronjs/esp/esp-idf/components/wifi_provisioning/Kconfig \
	/home/aaronjs/esp/esp-idf/components/app_update/Kconfig.projbuild \
	/home/aaronjs/esp/esp-idf/components/bootloader/Kconfig.projbuild \
	/home/aaronjs/esp/esp-idf/components/esptool_py/Kconfig.projbuild \
	/home/aaronjs/GitHub/Semester_6_Files/CS684/Labwork/Lab_0/Lab_0-ESP32/main/Kconfig.projbuild \
	/home/aaronjs/esp/esp-idf/components/partition_table/Kconfig.projbuild \
	/home/aaronjs/esp/esp-idf/Kconfig

include/config/auto.conf: \
	$(deps_config)

ifneq "$(IDF_TARGET)" "esp32"
include/config/auto.conf: FORCE
endif
ifneq "$(IDF_CMAKE)" "n"
include/config/auto.conf: FORCE
endif

$(deps_config): ;
