class CreateUndecidedSchedules < ActiveRecord::Migration[6.0]
  def change
    create_table :undecided_schedules do |t|
      t.string  :date
      t.integer :user_id
      t.string  :start_time
      t.string  :end_time
      t.boolean :is_confirmed, null: false, default: false

      t.timestamps
    end
  end
end
