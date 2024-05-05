from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Merhaba! Size nasıl yardımcı olabilirim?")
        return []

class ActionGoodbye(Action):
    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Görüşmek üzere! Başka bir şey için buradayım.")
        return []

class ActionAffirm(Action):
    def name(self) -> Text:
        return "action_affirm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Anladım, işlemi tamamlayacağım.")
        return []

class ActionDeny(Action):
    def name(self) -> Text:
        return "action_deny"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Anladım, işlemi iptal ediyorum.")
        return []

class ActionMoodGreat(Action):
    def name(self) -> Text:
        return "action_mood_great"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Harika! İyi hissettiğinize sevindim.")
        return []

class ActionMoodUnhappy(Action):
    def name(self) -> Text:
        return "action_mood_unhappy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Üzgünüm duydum. Size nasıl yardımcı olabilirim?")
        return []

class ActionBotChallenge(Action):
    def name(self) -> Text:
        return "action_bot_challenge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Evet, bir botum. Size nasıl yardımcı olabilirim?")
        return []

class ActionAskProduct(Action):
    def name(self) -> Text:
        return "action_ask_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ürün hakkında bir sorunuz var mı?")
        return []

class ActionAskPayment(Action):
    def name(self) -> Text:
        return "action_ask_payment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ödeme konusunda size nasıl yardımcı olabilirim?")
        return []

class ActionAskInvoice(Action):
    def name(self) -> Text:
        return "action_ask_invoice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Fatura bilgilerinizde yardımcı olabilir miyim?")
        return []

class ActionAskMusic(Action):
    def name(self) -> Text:
        return "action_ask_music"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Müzik dinlemek isterseniz, size Elma Müzik sitesini önerebilirim.")
        return []

class ActionAskForHelp(Action):
    def name(self) -> Text:
        return "action_ask_for_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Üzgünüm, size yardımcı olamadık. Nasıl yardımcı olabiliriz?")
        return []

class ActionOfferProduct(Action):
    def name(self) -> Text:
        return "action_offer_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ürün satın almak isterseniz, size yardımcı olabilirim.")
        return []

class ActionPaymentPage(Action):
    def name(self) -> Text:
        return "action_payment_page"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Fatura ödeme sayfasına gitmek için linke tıklayabilirsiniz: [Fatura Ödeme Sayfası](https://www.faturapay.com)")
        return []

class ActionDetailedInvoice(Action):
    def name(self) -> Text:
        return "action_detailed_invoice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ayrıntılı fatura bilgileriniz aşağıdaki gibidir: [Fatura Detayları](https://www.faturadetail.com)")
        return []

class ActionRedirectToMusicSite(Action):
    def name(self) -> Text:
        return "action_redirect_to_music_site"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Müzik dinlemek isterseniz, sizi Elma Müzik sitesine yönlendiriyorum. [Elma Müzik](https://www.elmamuzik.com)")
        return []

class ActionRedirectToCustomerService(Action):
    def name(self) -> Text:
        return "action_redirect_to_customer_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Müşteri hizmetlerine yönlendiriliyorsunuz. Size nasıl yardımcı olabiliriz?")
        return []

class ActionSadMood(Action):
    def name(self) -> Text:
        return "action_sad_mood"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="İsterseniz modunuzu yükseltecek hareketli şarkılar çalabilirim yada sizin için güzel arabesk şarkılar önerebilirim?")
        return []

class ActionFizySuggestion(Action):
    def name(self) -> Text:
        return "fizy_music_suggestion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Tabii ki, isterseniz güzel ve hareketli şarkılar önerebilirim")
        return []

class ChoosingSad(Action):
    def name(self) -> Text:
        return "choosing_sad"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Tabi ki size arabesk şarkılar öneriyorum")
        return []

class ChoosingHappy(Action):
    def name(self) -> Text:
        return "choosing_happy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Tabii ki! Size neşeli şarkılar öneriyorum.")
        return []

class ActionHappyMod(Action):
    def name(self) -> Text:
        return "action_happy_mood"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Bunu duyduğuma çok sevindim size hemen güzel ve hareketli şarkılar öneriyorum")
        return []

class ActionTrip(Action):
    def name(self) -> Text:
        return "action_trip"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Tabii ki size yolda dinlemelik bir playlist önerisi yapıcam")
        return []

class RapMusic(Action):
    def name(self) -> Text:
        return "rap_music"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Tabii ki, ama önce hangi tür rap dinlemek istediğinizi öğrenmem gerekir")
        return []

class TurkishRap(Action):
    def name(self) -> Text:
        return "turkish_rap_music"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Tabii ki, sana Türkçe güzel rapler önercem hem yeni hem eski tarzdan")
        return []

class YabanciRap(Action):
    def name(self) -> Text:
        return "yabanci_rap_music"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Tabii ki, yabancı rap listelerimden birini denemenizi isterim")
        return []

class OldSchoolRap(Action):
    def name(self) -> Text:
        return "oldschool_rap_music"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Tabii ki, zevkli bir adama benziyorsun sana hemen old school bir şeyler önericem")
        return []

class PlayRandomSong(Action):
    def name(self) -> Text:
        return "play_random_song_fizy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Tabii ki, size rastgele bir şarkı öneriyorum")
        return []

class PlayTopCharts(Action):
    def name(self) -> Text:
        return "play_top_charts_fizy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Tabii ki, fizydeki en popüler şakrılara yönlendiricem sizi")
        return []

class ActionPredictedIntent(Action):
    def name(self) -> Text:
        return "action_predicted_intent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        predicted_intent = tracker.latest_message['intent'].get('name')
        dispatcher.utter_message(text=f"Tahmin edilen niyet: {predicted_intent}")
        return []

class ActionPredictedIntent(Action):
    def name(self) -> Text:
        return "pasaj_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sizi pasaja yönlendiriyorum, pasaj Turkcell'in alış-veriş imkanı sunan sanal mağzasıdır.")
        return []

#SEBİL TARAFINDAN YAPILDI😮