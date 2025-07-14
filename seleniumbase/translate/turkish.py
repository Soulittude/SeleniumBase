# Turkish / Türkçe - Translations
from seleniumbase import BaseCase
from seleniumbase import MasterQA


class DurumTesti(BaseCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._language = "Turkish"

    def aç(self, *args, **kwargs):
        # open(url)
        return self.open(*args, **kwargs)

    def aç_url(self, *args, **kwargs):
        # open_url(url)
        return self.open_url(*args, **kwargs)

    def tıkla(self, *args, **kwargs):
        # click(selector)
        return self.click(*args, **kwargs)

    def çift_tıkla(self, *args, **kwargs):
        # double_click(selector)
        return self.double_click(*args, **kwargs)

    def bağlam_tıkla(self, *args, **kwargs):
        # context_click(selector)
        return self.context_click(*args, **kwargs)

    def yavaş_tıkla(self, *args, **kwargs):
        # slow_click(selector)
        return self.slow_click(*args, **kwargs)

    def eğer_görünüyorsa_tıkla(self, *args, **kwargs):
        # click_if_visible(selector, by=By.CSS_SELECTOR)
        return self.click_if_visible(*args, **kwargs)

    def eğer_görünüyorsa_js_tıkla(self, *args, **kwargs):
        # js_click_if_present(selector, by=By.CSS_SELECTOR)
        return self.js_click_if_present(*args, **kwargs)

    def bağlantı_yazısına_tıkla(self, *args, **kwargs):
        # click_link_text(link_text)
        return self.click_link_text(*args, **kwargs)

    def ofset_ile_tıkla(self, *args, **kwargs):
        # click_with_offset(selector, x, y, by=By.CSS_SELECTOR,
        #                   mark=None, timeout=None, center=None)
        return self.click_with_offset(*args, **kwargs)

    def yazıyı_güncelle(self, *args, **kwargs):
        # update_text(selector, text)
        return self.update_text(*args, **kwargs)

    def yaz(self, *args, **kwargs):
        # type(selector, text)  # Same as update_text()
        return self.type(*args, **kwargs)

    def yazı_ekle(self, *args, **kwargs):
        # add_text(selector, text)
        return self.add_text(*args, **kwargs)

    def yazı_al(self, *args, **kwargs):
        # get_text(selector, text)
        return self.get_text(*args, **kwargs)

    def yazı_kontrol(self, *args, **kwargs):
        # assert_text(text, selector)
        return self.assert_text(*args, **kwargs)

    def kesin_yazı_kontrol(self, *args, **kwargs):
        # assert_exact_text(text, selector)
        return self.assert_exact_text(*args, **kwargs)

    def bağlantı_metni_kontrol(self, *args, **kwargs):
        # assert_link_text(link_text)
        return self.assert_link_text(*args, **kwargs)

    def yazı_doluluk_kontrol(self, *args, **kwargs):
        # assert_non_empty_text(selector)
        return self.assert_non_empty_text(*args, **kwargs)

    def yazı_görünmezlik_kontrol(self, *args, **kwargs):
        # assert_text_not_visible(text, selector)
        return self.assert_text_not_visible(*args, **kwargs)

    def eleman_kontrol(self, *args, **kwargs):
        # assert_element(selector)
        return self.assert_element(*args, **kwargs)

    def eleman_görünür_kontrol(self, *args, **kwargs):
        # assert_element_visible(selector)  # Same as self.assert_element()
        return self.assert_element_visible(*args, **kwargs)

    def vérifier_élément_pas_affiché(self, *args, **kwargs):
        # assert_element_not_visible(selector)
        return self.assert_element_not_visible(*args, **kwargs)

    def eleman_görünmez_kontrol(self, *args, **kwargs):
        # assert_element_present(selector)
        return self.assert_element_present(*args, **kwargs)

    def eleman_yokluk_kontrol(self, *args, **kwargs):
        # assert_element_absent(selector)
        return self.assert_element_absent(*args, **kwargs)

    def özellik_kontrol(self, *args, **kwargs):
        # assert_attribute(selector, attribute, value)
        return self.assert_attribute(*args, **kwargs)

    def url_kontrol(self, *args, **kwargs):
        # assert_url(url)
        return self.assert_url(*args, **kwargs)

    def url_iceriyor_kontrol(self, *args, **kwargs):
        # assert_url_contains(substring)
        return self.assert_url_contains(*args, **kwargs)

    def başlık_kontrol(self, *args, **kwargs):
        # assert_title(title)
        return self.assert_title(*args, **kwargs)

    def başlık_iceriyor_kontrol(self, *args, **kwargs):
        # assert_title_contains(substring)
        return self.assert_title_contains(*args, **kwargs)

    def başlık_al(self, *args, **kwargs):
        # get_title()
        return self.get_title(*args, **kwargs)

    def doğru_kontrol(self, *args, **kwargs):
        # assert_true(expr)
        return self.assert_true(*args, **kwargs)

    def yanlış_kontrol(self, *args, **kwargs):
        # assert_false(expr)
        return self.assert_false(*args, **kwargs)

    def eşit_kontrol(self, *args, **kwargs):
        # assert_equal(first, second)
        return self.assert_equal(*args, **kwargs)

    def eşit_değil_kontrol(self, *args, **kwargs):
        # assert_not_equal(first, second)
        return self.assert_not_equal(*args, **kwargs)

    def sayfayı_yenile(self, *args, **kwargs):
        # refresh_page()
        return self.refresh_page(*args, **kwargs)

    def şimdiki_url_al(self, *args, **kwargs):
        # get_current_url()
        return self.get_current_url(*args, **kwargs)

    def sayfa_kaynağı_al(self, *args, **kwargs):
        # get_page_source()
        return self.get_page_source(*args, **kwargs)

    def geri_dön(self, *args, **kwargs):
        # go_back()
        return self.go_back(*args, **kwargs)

    def ileri_git(self, *args, **kwargs):
        # go_forward()
        return self.go_forward(*args, **kwargs)

    def yazı_görünüyor_mu(self, *args, **kwargs):
        # is_text_visible(text, selector="html")
        return self.is_text_visible(*args, **kwargs)

    def kesin_yazı_görünüyor_mu(self, *args, **kwargs):
        # is_exact_text_visible(text, selector="html")
        return self.is_exact_text_visible(*args, **kwargs)

    def eleman_görünüyor_mu(self, *args, **kwargs):
        # is_element_visible(selector)
        return self.is_element_visible(*args, **kwargs)

    def eleman_aktif_mi(self, *args, **kwargs):
        # is_element_enabled(selector)
        return self.is_element_enabled(*args, **kwargs)

    def eleman_mevcut_mu(self, *args, **kwargs):
        # is_element_present(selector)
        return self.is_element_present(*args, **kwargs)

    def yazı_için_bekle(self, *args, **kwargs):
        # wait_for_text(text, selector)
        return self.wait_for_text(*args, **kwargs)

    def eleman_için_bekle(self, *args, **kwargs):
        # wait_for_element(selector)
        return self.wait_for_element(*args, **kwargs)

    def elemanın_görünür_olmasını_bekle(self, *args, **kwargs):
        # wait_for_element_visible(selector)  # Same as wait_for_element()
        return self.wait_for_element_visible(*args, **kwargs)

    def elemanın_görünmez_olmasını_bekle(self, *args, **kwargs):
        # wait_for_element_not_visible(selector)
        return self.wait_for_element_not_visible(*args, **kwargs)

    def elemanın_mevcut_olmasını_bekle(self, *args, **kwargs):
        # wait_for_element_present(selector)
        return self.wait_for_element_present(*args, **kwargs)

    def elemanın_yok_olmasını_bekle(self, *args, **kwargs):
        # wait_for_element_absent(selector)
        return self.wait_for_element_absent(*args, **kwargs)

    def özellik_için_bekle(self, *args, **kwargs):
        # wait_for_attribute(selector, attribute, value)
        return self.wait_for_attribute(*args, **kwargs)

    def hazır_durumunun_bitmesini_bekle(self, *args, **kwargs):
        # wait_for_ready_state_complete()
        return self.wait_for_ready_state_complete(*args, **kwargs)

    def uyu(self, *args, **kwargs):
        # sleep(seconds)
        return self.sleep(*args, **kwargs)

    def bekle(self, *args, **kwargs):
        # wait(seconds)  # Same as sleep(seconds)
        return self.wait(*args, **kwargs)

    def gönder(self, *args, **kwargs):
        # submit(selector)
        return self.submit(*args, **kwargs)

    def temizle(self, *args, **kwargs):
        # clear(selector)
        return self.clear(*args, **kwargs)

    def odakla(self, *args, **kwargs):
        # focus(selector)
        return self.focus(*args, **kwargs)

    def js_tıkla(self, *args, **kwargs):
        # js_click(selector)
        return self.js_click(*args, **kwargs)

    def js_yazıyı_güncelle(self, *args, **kwargs):
        # js_update_text(selector, text)
        return self.js_update_text(*args, **kwargs)

    def js_yaz(self, *args, **kwargs):
        # js_type(selector, text)
        return self.js_type(*args, **kwargs)

    def jquery_tıkla(self, *args, **kwargs):
        # jquery_click(selector)
        return self.jquery_click(*args, **kwargs)

    def jquery_yazıyı_güncelle(self, *args, **kwargs):
        # jquery_update_text(selector, text)
        return self.jquery_update_text(*args, **kwargs)

    def jquery_yaz(self, *args, **kwargs):
        # jquery_type(selector, text)
        return self.jquery_type(*args, **kwargs)

    def html_incele(self, *args, **kwargs):
        # inspect_html()
        return self.inspect_html(*args, **kwargs)

    def ekran_görüntüsü_kaydet(self, *args, **kwargs):
        # save_screenshot(name)
        return self.save_screenshot(*args, **kwargs)

    def ekran_görüntüsünü_loglara_kaydet(self, *args, **kwargs):
        # save_screenshot_to_logs(name)
        return self.save_screenshot_to_logs(*args, **kwargs)

    def dosya_seç(self, *args, **kwargs):
        # choose_file(selector, file_path)
        return self.choose_file(*args, **kwargs)

    def script_çalıştır(self, *args, **kwargs):
        # execute_script(script)
        return self.execute_script(*args, **kwargs)

    def script_güvenli_çalıştır(self, *args, **kwargs):
        # safe_execute_script(script)
        return self.safe_execute_script(*args, **kwargs)

    def jquery_aktifleştir(self, *args, **kwargs):
        # activate_jquery()
        return self.activate_jquery(*args, **kwargs)

    def kaydedici_aktifleştir(self, *args, **kwargs):
        # activate_recorder()
        return self.activate_recorder(*args, **kwargs)

    def aç_eğer_url_değilse(self, *args, **kwargs):
        # open_if_not_url(url)
        return self.open_if_not_url(*args, **kwargs)

    def reklam_engelle(self, *args, **kwargs):
        # ad_block()
        return self.ad_block(*args, **kwargs)

    def atla(self, *args, **kwargs):
        # skip(reason="")
        return self.skip(*args, **kwargs)

    def kırık_link_kontrol(self, *args, **kwargs):
        # assert_no_404_errors()
        return self.assert_no_404_errors(*args, **kwargs)

    def js_hatası_yok_kontrol(self, *args, **kwargs):
        # assert_no_js_errors()
        return self.assert_no_js_errors(*args, **kwargs)

    def çerçeveye_geç(self, *args, **kwargs):
        # switch_to_frame(frame)
        return self.switch_to_frame(*args, **kwargs)

    def varsayılan_içeriğe_geç(self, *args, **kwargs):
        # switch_to_default_content()
        return self.switch_to_default_content(*args, **kwargs)

    def ebeveyn_çerçeveye_geç(self, *args, **kwargs):
        # switch_to_parent_frame()
        return self.switch_to_parent_frame(*args, **kwargs)

    def yeni_pencere_aç(self, *args, **kwargs):
        # open_new_window()
        return self.open_new_window(*args, **kwargs)

    def pencereye_geç(self, *args, **kwargs):
        # switch_to_window(window)
        return self.switch_to_window(*args, **kwargs)

    def varsayılan_pencereye_geç(self, *args, **kwargs):
        # switch_to_default_window()
        return self.switch_to_default_window(*args, **kwargs)

    def en_yeni_pencereye_geç(self, *args, **kwargs):
        # switch_to_newest_window()
        return self.switch_to_newest_window(*args, **kwargs)

    def pencereyi_büyüt(self, *args, **kwargs):
        # maximize_window()
        return self.maximize_window(*args, **kwargs)

    def vurgula(self, *args, **kwargs):
        # highlight(selector)
        return self.highlight(*args, **kwargs)

    def vurgu_tıkla(self, *args, **kwargs):
        # highlight_click(selector)
        return self.highlight_click(*args, **kwargs)

    def kaydır(self, *args, **kwargs):
        # scroll_to(selector)
        return self.scroll_to(*args, **kwargs)

    def en_üste_kaydır(self, *args, **kwargs):
        # scroll_to_top()
        return self.scroll_to_top(*args, **kwargs)

    def en_alta_kaydır(self, *args, **kwargs):
        # scroll_to_bottom()
        return self.scroll_to_bottom(*args, **kwargs)

    def üzerine_gel_ve_tıkla(self, *args, **kwargs):
        # hover_and_click(hover_selector, click_selector)
        return self.hover_and_click(*args, **kwargs)

    def üzerine_gel(self, *args, **kwargs):
        # hover(selector)
        return self.hover(*args, **kwargs)

    def seçili_mi(self, *args, **kwargs):
        # is_selected(selector)
        return self.is_selected(*args, **kwargs)

    def yukarı_ok_bas(self, *args, **kwargs):
        # press_up_arrow(selector="html", times=1)
        return self.press_up_arrow(*args, **kwargs)

    def aşağı_ok_bas(self, *args, **kwargs):
        # press_down_arrow(selector="html", times=1)
        return self.press_down_arrow(*args, **kwargs)

    def sol_ok_bas(self, *args, **kwargs):
        # press_left_arrow(selector="html", times=1)
        return self.press_left_arrow(*args, **kwargs)

    def sağ_ok_bas(self, *args, **kwargs):
        # press_right_arrow(selector="html", times=1)
        return self.press_right_arrow(*args, **kwargs)

    def görünür_elemanlara_tıkla(self, *args, **kwargs):
        # click_visible_elements(selector)
        return self.click_visible_elements(*args, **kwargs)

    def yazıya_göre_seçeneği_seç(self, *args, **kwargs):
        # select_option_by_text(dropdown_selector, option)
        return self.select_option_by_text(*args, **kwargs)

    def indekse_göre_seçenek_seç(self, *args, **kwargs):
        # select_option_by_index(dropdown_selector, option)
        return self.select_option_by_index(*args, **kwargs)

    def değere_göre_seçenek_seç(self, *args, **kwargs):
        # select_option_by_value(dropdown_selector, option)
        return self.select_option_by_value(*args, **kwargs)

    def sunum_oluştur(self, *args, **kwargs):
        # create_presentation(name=None, theme="default", transition="default")
        return self.create_presentation(*args, **kwargs)

    def slayt_ekle(self, *args, **kwargs):
        # add_slide(content=None, image=None, code=None, iframe=None,
        #           content2=None, notes=None, transition=None, name=None)
        return self.add_slide(*args, **kwargs)

    def slayt_kaydet(self, *args, **kwargs):
        # save_presentation(name=None, filename=None,
        #                   show_notes=False, interval=0)
        return self.save_presentation(*args, **kwargs)

    def slayt_başlat(self, *args, **kwargs):
        # begin_presentation(name=None, filename=None,
        #                    show_notes=False, interval=0)
        return self.begin_presentation(*args, **kwargs)

    def pasta_grafiği_oluştur(self, *args, **kwargs):
        # create_pie_chart(chart_name=None, title=None, subtitle=None,
        #                  data_name=None, unit=None, libs=True)
        return self.create_pie_chart(*args, **kwargs)

    def bar_grafiği_oluştur(self, *args, **kwargs):
        # create_bar_chart(chart_name=None, title=None, subtitle=None,
        #                  data_name=None, unit=None, libs=True)
        return self.create_bar_chart(*args, **kwargs)

    def sütun_grafiği_oluştur(self, *args, **kwargs):
        # create_column_chart(chart_name=None, title=None, subtitle=None,
        #                     data_name=None, unit=None, libs=True)
        return self.create_column_chart(*args, **kwargs)

    def çizgi_grafiği_oluştur(self, *args, **kwargs):
        # create_line_chart(chart_name=None, title=None, subtitle=None,
        #                   data_name=None, unit=None, zero=False, libs=True)
        return self.create_line_chart(*args, **kwargs)

    def bölge_grafiği_oluştur(self, *args, **kwargs):
        # create_area_chart(chart_name=None, title=None, subtitle=None,
        #                   data_name=None, unit=None, zero=False, libs=True)
        return self.create_area_chart(*args, **kwargs)

    def serileri_grafiğe_ekle(self, *args, **kwargs):
        # add_series_to_chart(data_name=None, chart_name=None)
        return self.add_series_to_chart(*args, **kwargs)

    def veri_noktası_ekle(self, *args, **kwargs):
        # add_data_point(label, value, color=None, chart_name=None)
        return self.add_data_point(*args, **kwargs)

    def grafik_kaydet(self, *args, **kwargs):
        # save_chart(chart_name=None, filename=None)
        return self.save_chart(*args, **kwargs)

    def grafik_göster(self, *args, **kwargs):
        # display_chart(chart_name=None, filename=None, interval=0)
        return self.display_chart(*args, **kwargs)

    def grafiği_çıkart(self, *args, **kwargs):
        # extract_chart(chart_name=None)
        return self.extract_chart(*args, **kwargs)

    def tur_oluştur(self, *args, **kwargs):
        # create_tour(name=None, theme=None)
        return self.create_tour(*args, **kwargs)

    def shepherd_turu_oluştur(self, *args, **kwargs):
        # create_shepherd_tour(name=None, theme=None)
        return self.create_shepherd_tour(*args, **kwargs)

    def bootstrap_turu_oluştur(self, *args, **kwargs):
        # create_bootstrap_tour(name=None, theme=None)
        return self.create_bootstrap_tour(*args, **kwargs)

    def driverjs_turu_oluştur(self, *args, **kwargs):
        # create_driverjs_tour(name=None, theme=None)
        return self.create_driverjs_tour(*args, **kwargs)

    def hopscotch_turu_oluştur(self, *args, **kwargs):
        # create_hopscotch_tour(name=None, theme=None)
        return self.create_hopscotch_tour(*args, **kwargs)

    def introjs_turu_oluştur(self, *args, **kwargs):
        # create_introjs_tour(name=None, theme=None)
        return self.create_introjs_tour(*args, **kwargs)

    def tur_adımı_ekle(self, *args, **kwargs):
        # add_tour_step(message, selector=None, name=None,
        #               title=None, theme=None, alignment=None)
        return self.add_tour_step(*args, **kwargs)

    def turu_oynat(self, *args, **kwargs):
        # play_tour(name=None)
        return self.play_tour(*args, **kwargs)

    def turu_aktar(self, *args, **kwargs):
        # export_tour(name=None, filename="my_tour.js", url=None)
        return self.export_tour(*args, **kwargs)

    def pdf_yazısı_al(self, *args, **kwargs):
        # get_pdf_text(pdf, page=None, maxpages=None, password=None,
        #              codec='utf-8', wrap=False, nav=False, override=False)
        return self.get_pdf_text(*args, **kwargs)

    def vérifier_texte_pdf(self, *args, **kwargs):
        # assert_pdf_text(pdf, text, page=None, maxpages=None, password=None,
        #                 codec='utf-8', wrap=True, nav=False, override=False)
        return self.assert_pdf_text(*args, **kwargs)

    def dosya_indir(self, *args, **kwargs):
        # download_file(file)
        return self.download_file(*args, **kwargs)

    def mevcut_dosya_indirildi_mi(self, *args, **kwargs):
        # is_downloaded_file_present(file)
        return self.is_downloaded_file_present(*args, **kwargs)

    def indirilen_dosyanın_dizini_al(self, *args, **kwargs):
        # get_path_of_downloaded_file(file)
        return self.get_path_of_downloaded_file(*args, **kwargs)

    def vérifier_fichier_téléchargé(self, *args, **kwargs):
        # assert_downloaded_file(file)
        return self.assert_downloaded_file(*args, **kwargs)

    def indirilen_dosyayı_sil(self, *args, **kwargs):
        # delete_downloaded_file(file)
        return self.delete_downloaded_file(*args, **kwargs)

    def başarısız(self, *args, **kwargs):
        # fail(msg=None)  # Inherited from "unittest"
        return self.fail(*args, **kwargs)

    def al(self, *args, **kwargs):
        # get(url)  # Same as open(url)
        return self.get(*args, **kwargs)

    def ziyaret(self, *args, **kwargs):
        # visit(url)  # Same as open(url)
        return self.visit(*args, **kwargs)

    def ziyaret_url(self, *args, **kwargs):
        # visit_url(url)  # Same as open(url)
        return self.visit_url(*args, **kwargs)

    def eleman_al(self, *args, **kwargs):
        # get_element(selector)  # Element can be hidden
        return self.get_element(*args, **kwargs)

    def eleman_bul(self, *args, **kwargs):
        # find_element(selector)  # Element must be visible
        return self.find_element(*args, **kwargs)

    def eleman_kaldır(self, *args, **kwargs):
        # remove_element(selector)
        return self.remove_element(*args, **kwargs)

    def elemanları_kaldır(self, *args, **kwargs):
        # remove_elements(selector)
        return self.remove_elements(*args, **kwargs)

    def yazı_bul(self, *args, **kwargs):
        # find_text(text, selector="html")  # Same as wait_for_text
        return self.find_text(*args, **kwargs)

    def yazı_ayarla(self, *args, **kwargs):
        # set_text(selector, text)
        return self.set_text(*args, **kwargs)

    def özellik_al(self, *args, **kwargs):
        # get_attribute(selector, attribute)
        return self.get_attribute(*args, **kwargs)

    def özellik_ayarla(self, *args, **kwargs):
        # set_attribute(selector, attribute, value)
        return self.set_attribute(*args, **kwargs)

    def özellik_ayarla(self, *args, **kwargs):
        # set_attributes(selector, attribute, value)
        return self.set_attributes(*args, **kwargs)

    def yaz(self, *args, **kwargs):
        # write(selector, text)  # Same as update_text()
        return self.write(*args, **kwargs)

    def mesajcı_temasını_ayarla(self, *args, **kwargs):
        # set_messenger_theme(theme="default", location="default")
        return self.set_messenger_theme(*args, **kwargs)

    def mesaj_gönder(self, *args, **kwargs):
        # post_message(message, duration=None, pause=True, style="info")
        return self.post_message(*args, **kwargs)

    def yazdır(self, *args, **kwargs):
        # _print(msg)  # Same as Python print()
        return self._print(*args, **kwargs)

    def ertelenmiş_eleman_kontrolü(self, *args, **kwargs):
        # deferred_assert_element(selector)
        return self.deferred_assert_element(*args, **kwargs)

    def ertelenmiş_yazı_kontrolü(self, *args, **kwargs):
        # deferred_assert_text(text, selector="html")
        return self.deferred_assert_text(*args, **kwargs)

    def ertelenmiş_kontroller_işle(self, *args, **kwargs):
        # process_deferred_asserts(print_only=False)
        return self.process_deferred_asserts(*args, **kwargs)

    def uyarı_kabul_et(self, *args, **kwargs):
        # accept_alert(timeout=None)
        return self.accept_alert(*args, **kwargs)

    def uyarıyı_kov(self, *args, **kwargs):
        # dismiss_alert(timeout=None)
        return self.dismiss_alert(*args, **kwargs)

    def uyarıya_geç(self, *args, **kwargs):
        # switch_to_alert(timeout=None)
        return self.switch_to_alert(*args, **kwargs)

    def sürükle_bırak(self, *args, **kwargs):
        # drag_and_drop(drag_selector, drop_selector)
        return self.drag_and_drop(*args, **kwargs)

    def içeriği_ayarla(self, *args, **kwargs):
        # set_content(html_string, new_page=False)
        return self.set_content(*args, **kwargs)

    def html_dosyası_yükle(self, *args, **kwargs):
        # load_html_file(html_file, new_page=True)
        return self.load_html_file(*args, **kwargs)

    def html_dosyası_al(self, *args, **kwargs):
        # open_html_file(html_file)
        return self.open_html_file(*args, **kwargs)

    def tüm_çerezleri_sil(self, *args, **kwargs):
        # delete_all_cookies()
        return self.delete_all_cookies(*args, **kwargs)

    def kullanıcı_aracısı_al(self, *args, **kwargs):
        # get_user_agent()
        return self.get_user_agent(*args, **kwargs)

    def lokal_kod_al(self, *args, **kwargs):
        # get_locale_code()
        return self.get_locale_code(*args, **kwargs)


class MasterQA_Turkish(MasterQA, DurumTesti):
    def kontrol(self, *args, **kwargs):
        # "Manual Check"
        self.DEFAULT_VALIDATION_TITLE = "Manuel kontrol"
        # "Does the page look good?"
        self.DEFAULT_VALIDATION_MESSAGE = "Sayfa doğru görünüyor mu?"
        # verify(QUESTION)
        return self.verify(*args, **kwargs)
